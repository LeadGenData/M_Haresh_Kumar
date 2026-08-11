# 📚 Master Technical Interview Question Bank — Scenario-Based Cupboard

This repository acts as your personal "technical interview cupboard", organized strictly by **Real-World Scenarios** that interviewers ask during senior technical rounds.

---

## 🏛️ SCENARIO 1: Data Pipeline Failure & Troubleshooting
* **Real-World Challenge:** A production data pipeline or Spark job fails at 4:55 PM on Friday or generates incomplete output.
* **Key Topics:** Error Log Isolation (Data vs. Code vs. Compute), ADF Pipeline Debugging, OOM Errors, Alerting & Recovery.
* **Reference Guides:**
  - 📄 [Wipro PySpark & Databricks Scenario Bank (Section 5)](./Wipro_PySpark_Databricks_ADF_Question_Bank.pdf)

---

## 🏛️ SCENARIO 2: Data Quality & Governance Audit
* **Real-World Challenge:** Raw incoming data contains nulls, invalid formats, or duplicate business keys before ingestion into enterprise reporting layers.
* **Key Topics:** Ingestion Quality Checks, Primary Key Deduplication (`ROW_NUMBER() OVER`), Exception Audit Tables, PII Masking.
* **Reference Guides:**
  - 📄 [Mphasis Data Governance Interview Prep Guide](../../../Desktop/Mphasis_Data_Governance_Interview_Prep_Guide.md)
  - 📄 [Wipro PySpark Data Validation (Section 1)](./Wipro_PySpark_Databricks_ADF_Question_Bank.pdf)

---

## 🏛️ SCENARIO 3: Medallion Lakehouse & Star-Schema Design
* **Real-World Challenge:** Transitioning raw source data into high-performance Silver/Gold layers for executive dashboards.
* **Key Topics:** Bronze (Raw) -> Silver (Cleansed) -> Gold (Business Aggregates), Star-Schema Modeling, Fact vs. Dimension Isolation.
* **Reference Guides:**
  - 📄 [Wipro Lakehouse & Medallion Architecture (Section 3)](./Wipro_PySpark_Databricks_ADF_Question_Bank.pdf)

---

## 🏛️ SCENARIO 4: Power BI & DAX Performance Optimization
* **Real-World Challenge:** Power BI reports taking 15+ seconds to render or crashing due to high VertiPaq memory consumption.
* **Key Topics:** VertiPaq Compression (DateTime splitting), `KEEPFILTERS` vs. `FILTER()`, Direct Lake vs. Import Mode.
* **Reference Guides:**
  - 📄 "The Comprehensive Power BI & Enterprise Business Intelligence Handbook" (Amazon KDP)

---

*Last Updated: Saturday, August 8, 2026*

---

## 🏛️ SCENARIO 5: Data Documentation & Business Requirements (BRD vs. FRS & KPI vs. KRI)
* **Real-World Challenge:** Translating business stakeholder expectations into technical data engineering and reporting specifications.
* **Key Definitions & Explanations:**
  - **BRD (Business Requirements Document):** High-level document created with business owners defining *WHAT* the business wants to achieve (e.g. "We need to track daily revenue across 20 countries").
  - **FRS (Functional Requirements Specification):** Detailed technical document created for data engineers/developers defining *HOW* the system will build it (e.g. "Table schema, SQL join logic, API endpoints, refresh frequencies").
  - **KPI (Key Performance Indicator):** Business growth metric (e.g. Monthly Revenue, Active Users).
  - **KRI (Key Risk Indicator):** Data quality risk metric (e.g. Data Error Rate, Missing Null %, SLA Breaches).
  - **KIS / SLA (Key Indicator Specs / Service Level Agreement):** Delivery uptime and turnaround standards (e.g. 99.9% report refresh uptime).

---

## 🏛️ SCENARIO 6: Power BI Workspace Roles & Data Access Control
* **Real-World Challenge:** Managing security, dataset publishing, and access permissions across enterprise Power BI workspaces.
* **The 4 Official Power BI Workspace Roles:**
  1. **Admin:** Full workspace control (add/remove users, delete workspace, manage permissions).
  2. **Member:** Can add users with lower permissions, publish reports, edit items, and create reports from workspace datasets.
  3. **Contributor:** Can create, edit, and delete reports/datasets inside the workspace (cannot add users or modify workspace settings).
  4. **Viewer:** Read-only access to view reports and dashboards (cannot edit or download semantic models).

---

## 🏛️ SCENARIO 7: Data Masking & PII Security Protection
* **Real-World Challenge:** Protecting sensitive customer data (SSN, Credit Card numbers, Phone numbers) from unauthorized viewing.
* **Types of Data Masking:**
  1. **Dynamic Data Masking (DDM):** Obfuscates sensitive data on-the-fly when queried (e.g. showing `XXXX-XXXX-1234` for credit cards while leaving underlying data intact).
  2. **Static Data Masking:** Permanently scrambles sensitive columns in non-production test/dev databases.
  3. **SQL Implementation:** Using `MASKING POLICY` in Snowflake or Dynamic Data Masking (`MASKED WITH (FUNCTION = 'partial(...)')`) in SQL Server.

---

## 🐍 SCENARIO 8: Processing Large Data Files in Python (Memory Optimization)
* **Real-World Challenge:** Reading giant multi-gigabyte CSV or JSON data files (5GB – 50GB+) that exceed available RAM without causing Out-Of-Memory (OOM) crashes.
* **The 4 Practical Python Approaches:**
  1. **Pandas `chunksize` (Chunking):** Process the file in smaller batches (e.g. 50,000 rows at a time).
     ```python
     import pandas as pd
     for chunk in pd.read_csv('large_file.csv', chunksize=50000):
         # Process each chunk independently
         process(chunk)
     ```
  2. **PySpark / Databricks (Distributed Processing):** Use PySpark DataFrame reader to process files across parallel worker nodes.
     ```python
     df = spark.read.csv('large_file.csv', header=True)
     ```
  3. **Polars / Dask (Out-of-Core Execution):** Use modern high-performance libraries like `polars.scan_csv()` or `dask.dataframe` for lazy evaluation.
  4. **Line-by-Line Generator Iteration:** Use native Python line generators for lightweight stream parsing.

---

## 📊 SCENARIO 9: Data Quality KPIs & Dashboard Visualizations
* **Real-World Challenge:** Defining practical data validation KPIs and choosing the right Power BI visuals for executive reporting.
* **Haresh's Operational KPI Formula:**
  - **Missing Email Variance:** `Total_Emails - Valid_Emails = Missing_Email_Count`
  - **Data Quality Variance %:** `(Total_Records - Valid_Records) / Total_Records * 100`
* **Recommended Power BI Visualizations:**
  - **Clustered Column Chart / Bar Chart:** Comparing Valid vs. Missing records across source batches.
  - **Time Series Line Chart:** Tracking data quality variance and error trends over time.
  - **KPI Cards:** Displaying Total Record Count and Data Quality Pass Rate %.

---

## 🏛️ SCENARIO 10: Medallion Architecture Layers (Bronze, Silver, Gold Data Engineering)
* **Real-World Challenge:** Structuring enterprise data pipelines into multi-stage Medallion architecture layers for storage, transformation, and BI consumption.
* **The 3 Core Medallion Layers:**
  1. **Bronze Layer (Raw Ingestion / Landing):**
     - **Purpose:** Raw data landing zone.
     - **What Happens Here:** Ingesting raw CSV/JSON/Kafka streams as-is from source systems without modification. Retains full history and append-only raw structure.
  2. **Silver Layer (Cleaned & Enriched / Validation):**
     - **Purpose:** Curated, cleaned, and validated data layer.
     - **What Happens Here:** Data Quality checks, primary key deduplication (`ROW_NUMBER() OVER`), null handling, data type casting, and schema enforcement. Bad records are routed to Exception tables.
  3. **Gold Layer (Business Aggregations / Semantic Model):**
     - **Purpose:** Star-Schema business reporting layer for Power BI / Fabric / Snowflake.
     - **What Happens Here:** Creating Fact and Dimension tables, pre-aggregated business KPIs, and single-source-of-truth semantic models for executive dashboards.

---

## 🏛️ SCENARIO 11: Governance Enforcement Across Data Architecture Layers
* **Real-World Challenge:** Where to enforce specific Data Governance rules (PII Masking, Access Security, Quality Controls, Metric Governance) across system layers.
* **Layer-by-Layer Data Governance Enforcement:**
  1. **Ingestion / Database Layer (Security & PII Governance):**
     - Enforcing **Dynamic Data Masking (DDM)** on PII columns (`Credit_Card`, `SSN`) using Snowflake Masking Policies or SQL Server Masking.
     - Enforcing **Row-Level Security (RLS)** and Role-Based Access Control (RBAC) at the database schema level.
  2. **Transformation / ETL Layer (Quality & Audit Governance):**
     - Enforcing **Data Quality Rules**, primary key deduplication (`ROW_NUMBER() OVER`), and exception logging into Audit tables.
  3. **Semantic / Power BI Layer (Metric & Definition Governance):**
     - Enforcing **Metric Governance** (single-source-of-truth DAX measures) and Object-Level Security (OLS) on business scorecards so executive leadership sees identical KPIs.
