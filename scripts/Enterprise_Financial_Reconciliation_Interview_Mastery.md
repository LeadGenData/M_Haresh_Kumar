# 🛡️ Enterprise Financial Reconciliation & Revenue Audit Framework

**Author:** M. Haresh Kumar — Data Operations Lead & Analytics Specialist (14+ Years Leadership)  
**Target Roles:** Data Operations Lead, Data Quality Assurance Analyst, Senior Analytics Specialist, Data Engineer (Reporting)  
**Assets:** `enterprise_financial_reconciliation.sql` | `run_reconciliation_audit.py`

---

## 🎯 The Core Business Problem (Why This Beats Theory)

In mid-sized and enterprise companies ($10M to $500M revenue), financial reporting breaks because data traverses multiple disjointed systems:

1. **Tier 1 (Source ERP / CRM):** Salesforce, SAP, QuickBooks, or proprietary billing databases where raw transactions are created.
2. **Tier 2 (Ingestion Lakehouse):** Snowflake, BigQuery, or Databricks bronze/silver staging layers where data is ingested via CDC or batch ETL.
3. **Tier 3 (Gold BI Reporting Mart):** Aggregated dimensional star-schema models feeding executive Power BI dashboards.

### The Silent Killer

A simple network timeout, schema alteration, or lagging CDC stream can drop 2 invoices out of 500. To an engineer looking only at row counts, `498` looks close to `500`. But if those two dropped invoices were commercial contracts worth **$10,450.00**, the CFO reports misleading revenue figures to the Board of Directors.

---

## 🏗️ The 3-Tier Production Architecture

```text
[ Tier 1: Source ERP ]  ───(ETL / CDC Pipeline)───► [ Tier 2: Snowflake Lakehouse ] ───► [ Tier 3: Gold BI Mart ]
  raw_erp_invoices                                     silver_clean_invoices                 fct_revenue_invoices
         │                                                                                          │
         └───────────────────────── FULL OUTER JOIN (Recon Engine) ─────────────────────────────────┘
                                                  │
                                                  ▼
                        [ Automated Exception & Discrepancy Log Table ]
                        • DROPPED_INVOICE (Missing in Mart) -> CRITICAL
                        • PHANTOM_RECORD (Orphan in Mart)   -> CRITICAL
                        • PRICING_DISCREPANCY (Drift > $0) -> HIGH
                        • STATUS_DESYNC (CDC Latency)       -> MEDIUM
```

---

## 💡 How to Answer the Question in an Interview

### Interviewer Question

> *"How do you ensure data accuracy, pipeline completeness, and reconcile numbers between your raw transaction systems and downstream reporting tables?"*

### Haresh's 10/10 Grounded Response

> *"Throughout my 14+ years in data operations, I never rely on spot-checks or single-table row counts. I implement an automated **dual-direction, 3-tier financial reconciliation framework**.*
>
> *First, at the **aggregate level**, my pipeline executes daily control-total queries across source and target marts, verifying not just row counts, but total gross revenue, sales tax, and net cash within a zero-tolerance threshold (`ABS(variance) < 0.01`).*
>
> *Second, at the **granular line level**, I execute a `FULL OUTER JOIN` on the primary transactional key (`invoice_id`). This immediately isolates four distinct production failure modes:*
>
> 1. *`DROPPED_INVOICE`: Records present in the source ERP that silently dropped during ETL ingestion.*
> 2. *`PHANTOM_RECORD`: Orphan records created downstream that have no verified source transaction.*
> 3. *`PRICING_DISCREPANCY`: Rounding errors or unapplied discount overrides where `src.amount <> tgt.amount`.*
> 4. *`STATUS_DESYNC`: Records where payment status is out of sync due to CDC replication latency (e.g., Paid in source, but still Pending in the BI mart).*
>
> *Any discrepancy exceeding threshold triggers an automated severity alert (`CRITICAL`, `HIGH`, `MEDIUM`) with the exact primary key, preventing erroneous numbers from ever reaching executive Power BI reports."*

---

## 💻 Technical Code Highlights (`enterprise_financial_reconciliation.sql`)

### 1. Dual-Direction Exception Matching via FULL OUTER JOIN

```sql
SELECT
    COALESCE(src.invoice_id, tgt.invoice_id) AS invoice_id,
    COALESCE(src.net_amount, 0) AS src_amount,
    COALESCE(tgt.net_amount, 0) AS tgt_amount,
    ROUND(COALESCE(src.net_amount, 0) - COALESCE(tgt.net_amount, 0), 2) AS amount_diff,
    CASE
        WHEN tgt.invoice_id IS NULL THEN 'DROPPED_INVOICE (MISSING_IN_MART)'
        WHEN src.invoice_id IS NULL THEN 'PHANTOM_RECORD (ORPHAN_IN_MART)'
        WHEN ABS(src.net_amount - tgt.net_amount) > 0.01 THEN 'PRICING_DISCREPANCY'
        WHEN src.payment_status <> tgt.payment_status THEN 'STATUS_DESYNC'
        ELSE 'PERFECT_MATCH'
    END AS discrepancy_type
FROM raw_erp_invoices src
FULL OUTER JOIN fct_revenue_invoices tgt
    ON src.invoice_id = tgt.invoice_id
WHERE discrepancy_type <> 'PERFECT_MATCH';
```

### 2. Live Python Verification (run_reconciliation_audit.py)

Can be executed live from the terminal in 3 seconds to demonstrate real-time audit output to technical interviewers.
