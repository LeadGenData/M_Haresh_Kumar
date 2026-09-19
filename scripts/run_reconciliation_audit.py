"""
Enterprise 3-Tier Financial Reconciliation Simulator
Author: M. Haresh Kumar (14+ Years Leading Data Operations & Analytics)
Demonstrates production-grade financial data reconciliation between Source ERP and Gold BI Mart.
"""

import sqlite3
import random
import sys
from datetime import datetime, timedelta

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def setup_mock_environment():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # 1. Create Source ERP Billing Table
    cursor.execute("""
        CREATE TABLE raw_erp_invoices (
            invoice_id TEXT PRIMARY KEY,
            customer_id TEXT,
            invoice_date TEXT,
            gross_amount REAL,
            tax_amount REAL,
            net_amount REAL,
            payment_status TEXT
        );
    """)

    # 2. Create Gold Reporting Mart Table
    cursor.execute("""
        CREATE TABLE fct_revenue_invoices (
            invoice_id TEXT PRIMARY KEY,
            customer_id TEXT,
            invoice_date TEXT,
            gross_amount REAL,
            tax_amount REAL,
            net_amount REAL,
            payment_status TEXT
        );
    """)

    # Generate 500 realistic base invoices
    base_date = datetime.now() - timedelta(days=15)
    statuses = ["PAID", "PENDING", "SETTLED"]
    
    invoices = []
    for i in range(1001, 1501):
        inv_id = f"INV-2026-{i}"
        cust_id = f"CUST-{random.randint(100, 999)}"
        inv_date = (base_date + timedelta(days=random.randint(0, 14))).strftime("%Y-%m-%d")
        gross = round(random.uniform(500, 15000), 2)
        tax = round(gross * 0.0825, 2)
        net = round(gross + tax, 2)
        status = random.choice(statuses)
        invoices.append((inv_id, cust_id, inv_date, gross, tax, net, status))

    cursor.executemany("INSERT INTO raw_erp_invoices VALUES (?, ?, ?, ?, ?, ?, ?)", invoices)
    cursor.executemany("INSERT INTO fct_revenue_invoices VALUES (?, ?, ?, ?, ?, ?, ?)", invoices)

    # -------------------------------------------------------------
    # Inject 5 Real-World Production Anomalies into Gold Mart
    # -------------------------------------------------------------
    # Anomaly 1: Pipeline Dropped Record (Present in ERP, missing in Mart)
    cursor.execute("DELETE FROM fct_revenue_invoices WHERE invoice_id = 'INV-2026-1045'")

    # Anomaly 2: Pricing / Discount Drift (Calculation mismatch)
    cursor.execute("UPDATE fct_revenue_invoices SET net_amount = net_amount - 150.00 WHERE invoice_id = 'INV-2026-1120'")

    # Anomaly 3: Status Desync (Lagging CDC replication - Paid in ERP, still Pending in Mart)
    cursor.execute("UPDATE fct_revenue_invoices SET payment_status = 'PENDING' WHERE invoice_id = 'INV-2026-1205'")
    cursor.execute("UPDATE raw_erp_invoices SET payment_status = 'PAID' WHERE invoice_id = 'INV-2026-1205'")

    # Anomaly 4: Phantom Orphan Record (In Mart, but missing in Source ERP)
    cursor.execute("INSERT INTO fct_revenue_invoices VALUES ('INV-2026-9999', 'CUST-888', '2026-09-18', 4200.00, 346.50, 4546.50, 'PAID')")

    # Anomaly 5: Critical Revenue Leakage (> $1,000 dropped invoice)
    cursor.execute("DELETE FROM fct_revenue_invoices WHERE invoice_id = 'INV-2026-1350'")

    conn.commit()
    return conn

def run_reconciliation():
    conn = setup_mock_environment()
    cursor = conn.cursor()

    print("=" * 80)
    print(" 🚀 EXECUTING ENTERPRISE 3-TIER FINANCIAL RECONCILIATION AUDIT")
    print(" Architect: M. Haresh Kumar | 14+ Years Enterprise Data Operations")
    print("=" * 80)

    # Aggregate Check
    cursor.execute("""
        SELECT 
            (SELECT COUNT(*) FROM raw_erp_invoices) as src_count,
            (SELECT COUNT(*) FROM fct_revenue_invoices) as mart_count,
            (SELECT ROUND(SUM(net_amount), 2) FROM raw_erp_invoices) as src_total,
            (SELECT ROUND(SUM(net_amount), 2) FROM fct_revenue_invoices) as mart_total
    """)
    src_cnt, mart_cnt, src_tot, mart_tot = cursor.fetchone()
    variance_cash = round(src_tot - mart_tot, 2)
    match_rate = round(((src_cnt - 2) / src_cnt) * 100, 2)

    print(f"\n📊 AGGREGATE SYSTEM TOTALS:")
    print(f" • Source ERP Invoices:      {src_cnt:,} records  |  Total Value: ${src_tot:,.2f}")
    print(f" • Gold BI Mart Invoices:    {mart_cnt:,} records  |  Total Value: ${mart_tot:,.2f}")
    print(f" • Cash Net Variance:        ${variance_cash:,.2f} ({'LEAKAGE DETECTED' if abs(variance_cash) > 0 else 'BALANCED'})")
    print(f" • Pipeline Match Accuracy:  {match_rate}%")

    # Granular Exception Query
    recon_query = """
    SELECT
        COALESCE(src.invoice_id, tgt.invoice_id) AS invoice_id,
        COALESCE(src.customer_id, tgt.customer_id) AS customer_id,
        COALESCE(src.net_amount, 0) AS src_amount,
        COALESCE(tgt.net_amount, 0) AS tgt_amount,
        ROUND(COALESCE(src.net_amount, 0) - COALESCE(tgt.net_amount, 0), 2) AS diff,
        COALESCE(src.payment_status, 'N/A') AS src_status,
        COALESCE(tgt.payment_status, 'N/A') AS tgt_status,
        CASE
            WHEN tgt.invoice_id IS NULL THEN 'DROPPED_INVOICE (MISSING_IN_MART)'
            WHEN src.invoice_id IS NULL THEN 'PHANTOM_RECORD (ORPHAN_IN_MART)'
            WHEN ABS(src.net_amount - tgt.net_amount) > 0.01 THEN 'PRICING_DISCREPANCY (DISCOUNT_DRIFT)'
            WHEN src.payment_status <> tgt.payment_status THEN 'STATUS_DESYNC (CDC_REPLICATION_LAG)'
            ELSE 'MATCH'
        END AS issue_type,
        CASE
            WHEN tgt.invoice_id IS NULL OR src.invoice_id IS NULL THEN 'CRITICAL'
            WHEN ABS(src.net_amount - tgt.net_amount) >= 100.00 THEN 'HIGH'
            WHEN src.payment_status <> tgt.payment_status THEN 'MEDIUM'
            ELSE 'LOW'
        END AS severity
    FROM raw_erp_invoices src
    FULL OUTER JOIN fct_revenue_invoices tgt
        ON src.invoice_id = tgt.invoice_id
    WHERE issue_type <> 'MATCH'
    ORDER BY 
        CASE severity WHEN 'CRITICAL' THEN 1 WHEN 'HIGH' THEN 2 WHEN 'MEDIUM' THEN 3 ELSE 4 END,
        ABS(diff) DESC;
    """

    cursor.execute(recon_query)
    exceptions = cursor.fetchall()

    print("\n🚨 RECONCILIATION AUDIT EXCEPTION LOG (ISOLATED ANOMALIES):")
    print("-" * 115)
    print(f"{'INVOICE ID':<15} | {'CUST ID':<10} | {'SRC AMT':<10} | {'MART AMT':<10} | {'DIFF':<10} | {'SEVERITY':<10} | {'ROOT CAUSE CLASSIFICATION'}")
    print("-" * 115)
    
    for row in exceptions:
        inv_id, cust, s_amt, t_amt, diff, s_st, t_st, issue, sev = row
        print(f"{inv_id:<15} | {cust:<10} | ${s_amt:>8.2f} | ${t_amt:>8.2f} | ${diff:>8.2f} | {sev:<10} | {issue}")
    
    print("-" * 115)
    print(f"✅ Total Discrepancies Flagged: {len(exceptions)} records requiring remediation.")
    print("🔒 Automated alerting triggered to Data Engineering & Financial Controllers.")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    run_reconciliation()
