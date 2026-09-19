-- ==============================================================================
-- ENTERPRISE 3-TIER FINANCIAL RECONCILIATION & REVENUE AUDIT FRAMEWORK
-- Author: M. Haresh Kumar (14+ Years Data Operations & Analytics Leadership)
-- Architecture: Source ERP Billing -> Ingestion Lakehouse -> Gold Reporting Mart
-- ==============================================================================

-- PURPOSE:
-- Eliminate silent revenue leakage and financial discrepancy between upstream
-- billing platforms (e.g., Salesforce, SAP, QuickBooks) and analytical reporting marts
-- feeding CFO Power BI executive dashboards.

-- ------------------------------------------------------------------------------
-- 1. STAGE LEVEL AGGREGATE RECONCILIATION (ROW COUNT & CASH CONTROL TOTALS)
-- ------------------------------------------------------------------------------
WITH source_daily_summary AS (
    SELECT
        CAST(invoice_date AS DATE) AS recon_date,
        COUNT(DISTINCT invoice_id) AS src_invoice_count,
        SUM(gross_amount)          AS src_total_gross,
        SUM(tax_amount)            AS src_total_tax,
        SUM(net_amount)            AS src_total_net
    FROM raw_erp_invoices
    WHERE invoice_date >= DATEADD(day, -30, CURRENT_DATE())
    GROUP BY CAST(invoice_date AS DATE)
),
mart_daily_summary AS (
    SELECT
        CAST(invoice_date AS DATE) AS recon_date,
        COUNT(DISTINCT invoice_id) AS mart_invoice_count,
        SUM(gross_amount)          AS mart_total_gross,
        SUM(tax_amount)            AS mart_total_tax,
        SUM(net_amount)            AS mart_total_net
    FROM fct_revenue_invoices
    WHERE invoice_date >= DATEADD(day, -30, CURRENT_DATE())
    GROUP BY CAST(invoice_date AS DATE)
)
SELECT
    COALESCE(s.recon_date, m.recon_date) AS recon_date,
    COALESCE(s.src_invoice_count, 0)     AS src_count,
    COALESCE(m.mart_invoice_count, 0)    AS mart_count,
    (COALESCE(s.src_invoice_count, 0) - COALESCE(m.mart_invoice_count, 0)) AS count_variance,
    
    COALESCE(s.src_total_net, 0.00)      AS src_net_revenue,
    COALESCE(m.mart_total_net, 0.00)     AS mart_net_revenue,
    ROUND(COALESCE(s.src_total_net, 0.00) - COALESCE(m.mart_total_net, 0.00), 2) AS cash_variance,
    
    CASE 
        WHEN COALESCE(s.src_invoice_count, 0) = COALESCE(m.mart_invoice_count, 0)
         AND ABS(COALESCE(s.src_total_net, 0.00) - COALESCE(m.mart_total_net, 0.00)) < 0.01 
        THEN 'CLEAN_RECONCILED'
        WHEN ABS(COALESCE(s.src_total_net, 0.00) - COALESCE(m.mart_total_net, 0.00)) >= 1000.00
        THEN 'CRITICAL_LEAKAGE_ALERT'
        ELSE 'VARIANCE_INVESTIGATION_REQUIRED'
    END AS audit_status
FROM source_daily_summary s
FULL OUTER JOIN mart_daily_summary m
    ON s.recon_date = m.recon_date
ORDER BY recon_date DESC;

-- ------------------------------------------------------------------------------
-- 2. GRANULAR LINE-BY-LINE EXCEPTION ENGINE (DISCREPANCY ISOLATION)
-- ------------------------------------------------------------------------------
WITH granular_match AS (
    SELECT
        COALESCE(src.invoice_id, tgt.invoice_id)     AS invoice_id,
        src.customer_id                             AS src_customer_id,
        tgt.customer_id                             AS tgt_customer_id,
        src.invoice_date                            AS src_invoice_date,
        tgt.invoice_date                            AS tgt_invoice_date,
        src.net_amount                              AS src_amount,
        tgt.net_amount                              AS tgt_amount,
        ROUND(COALESCE(src.net_amount, 0) - COALESCE(tgt.net_amount, 0), 2) AS amount_diff,
        src.payment_status                          AS src_status,
        tgt.payment_status                          AS tgt_status,
        
        -- Categorization Rules
        CASE
            WHEN tgt.invoice_id IS NULL 
                THEN 'MISSING_IN_REPORTING_MART (DROPPED_PIPELINE_RECORD)'
            WHEN src.invoice_id IS NULL 
                THEN 'PHANTOM_RECORD_IN_MART (ORPHAN_SYNTHETIC_DATA)'
            WHEN ABS(src.net_amount - tgt.net_amount) > 0.01 
                THEN 'AMOUNT_MISMATCH (ROUNDING_OR_DISCOUNT_DRIFT)'
            WHEN src.payment_status <> tgt.payment_status 
                THEN 'STATUS_DESYNCHRONIZATION (LAGGING_CDC_REPLICATION)'
            ELSE 'PERFECT_MATCH'
        END AS discrepancy_type,
        
        -- Severity Tier
        CASE
            WHEN tgt.invoice_id IS NULL OR src.invoice_id IS NULL 
                THEN 'CRITICAL'
            WHEN ABS(src.net_amount - tgt.net_amount) >= 100.00 
                THEN 'HIGH'
            WHEN src.payment_status <> tgt.payment_status 
                THEN 'MEDIUM'
            WHEN ABS(src.net_amount - tgt.net_amount) > 0.01 
                THEN 'LOW'
            ELSE 'NONE'
        END AS alert_severity
    FROM raw_erp_invoices src
    FULL OUTER JOIN fct_revenue_invoices tgt
        ON src.invoice_id = tgt.invoice_id
)
SELECT
    invoice_id,
    src_customer_id,
    tgt_customer_id,
    src_amount,
    tgt_amount,
    amount_diff,
    src_status,
    tgt_status,
    discrepancy_type,
    alert_severity,
    CURRENT_TIMESTAMP() AS audited_at
FROM granular_match
WHERE discrepancy_type <> 'PERFECT_MATCH'
ORDER BY 
    CASE alert_severity 
        WHEN 'CRITICAL' THEN 1 
        WHEN 'HIGH' THEN 2 
        WHEN 'MEDIUM' THEN 3 
        ELSE 4 
    END,
    ABS(amount_diff) DESC;
