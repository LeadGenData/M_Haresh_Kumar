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

---

## 📊 SCENARIO 12: Power BI DAX Query View Native Measure Documentation (`///` Syntax & TMDL)
* **Real-World Challenge:** Documenting DAX measures natively inside semantic models for AI Copilot context, metadata Q&A engines, and Git source control.
* **The New DAX Query View Syntax:**
  - Using `///` comments directly above `DEFINE MEASURE` saves metadata directly into the Tabular Model Definition Language (TMDL).
  ```dax
  /// Calculates total net sales revenue excluding returned items and applies explicit date filters
  DEFINE MEASURE 'Sales'[Net Revenue] = SUMX('Sales', 'Sales'[Quantity] * 'Sales'[Unit_Price])
  ```
* **Why This Matters for Enterprise Governance:**
  1. **Copilot & AI Context:** Prevents LLM hallucinations when querying semantic models by providing explicit business definitions.
  2. **Metadata Enriched Q&A:** Allows executive leadership to ask natural language Q&A questions with 100% accurate measure matching.
  3. **TMDL & Git Integration:** Enables automated documentation, CI/CD pipeline deployment, and version control across data teams.

---

## 🤖 SCENARIO 13: Microsoft Build 2026 Agentic Analytics & Fabric Innovations
* **Real-World Challenge:** Leveraging cutting-edge 2026 Microsoft Build agentic BI tools, Rayfin SDK, and Outbound Access Protection.
* **The 4 Key 2026 Innovations:**
  1. **Agent Skills for Power BI:** AI Agents (GitHub Copilot / Antigravity) use structured Skills & Tools (MCP) to generate semantic models, author reports from natural language or screenshots, and validate PBIP files.
  2. **Rayfin SDK (Backend-as-a-Service for Fabric):** Open-source TypeScript SDK (`@entity()`, `@text()`) compiling code-first definitions directly into Fabric GraphQL endpoints and database schemas.
  3. **Fabric Apps for Semantic Models:** Workspace item type allowing AI agents to scaffold, build, and deploy full-stack web applications on top of governed Power BI semantic models.
  4. **Outbound Access Protection (OAP):** Workspace-level security policy that blocks outbound public data connections by default, enforcing bound connections at the Power Query/DAX layer.

---

## ⚡ SCENARIO 14: Batch Processing Across SQL, Python, dbt, and Snowflake
* **Real-World Challenge:** Processing multi-gigabyte/terabyte data streams in structured batches to optimize memory usage, lower execution costs, and prevent system timeouts.

### 1. 🛢️ SQL Batching (Using Modulo & Date Range Iteration)
```sql
-- Batching by Date Ranges (e.g. Daily / Hourly Batches)
INSERT INTO Target_Table
SELECT * 
FROM Source_Staging
WHERE Ingestion_Date = '2026-08-10';

-- Batching large integer IDs using Modulo Arithmetic
SELECT * 
FROM Customer_Staging
WHERE MOD(Customer_ID, 10) = 0; -- Process 10% batch per run
```

### 2. 🐍 Python Batching (Pandas `chunksize` & Generators)
```python
import pandas as pd

# Processing 50,000 rows per batch chunk
chunk_size = 50000
for chunk_df in pd.read_csv("giant_file.csv", chunksize=chunk_size):
    # Perform cleaning and transformation on each batch
    chunk_df['Email'] = chunk_df['Email'].str.lower()
    # Append batch to database or target CSV
    chunk_df.to_sql("target_table", engine, if_exists="append", index=False)
```

### 3. 🛠️ dbt Incremental Batching (`is_incremental()`)
```sql
-- dbt Incremental Model Batching
{{
    config(
        materialized='incremental',
        unique_key='transaction_id'
    )
}}

SELECT *
FROM {{ ref('raw_transactions') }}
{% if is_incremental() %}
  -- Only process new batch records since the last run timestamp
  WHERE transaction_timestamp > (SELECT MAX(transaction_timestamp) FROM {{ this }})
{% endif %}
```

### 4. ❄️ Snowflake Streams & Tasks (Change Data Capture Batching)
```sql
-- Create a Change Data Capture Stream on Source Table
CREATE OR REPLACE STREAM Source_Table_Stream ON TABLE Source_Staging;

-- Scheduled Task to process stream delta in hourly batches
CREATE OR REPLACE TASK Process_Batch_Task
  WAREHOUSE = COMPUTE_WH
  SCHEDULE = 'USING CRON 0 * * * * UTC'
WHEN SYSTEM$STREAM_HAS_DATA('Source_Table_Stream')
AS
  MERGE INTO Target_Table T
  USING Source_Table_Stream S
  ON T.Customer_ID = S.Customer_ID
  WHEN MATCHED THEN UPDATE SET T.Email = S.Email
  WHEN NOT MATCHED THEN INSERT (Customer_ID, Email) VALUES (S.Customer_ID, S.Email);
```

---

## 🐍 SCENARIO 15: Core Python Data Structures (Tuples, Dictionaries, Lists & DataFrames)
* **Real-World Challenge:** Understanding standard Python data structures and how they interact with Pandas DataFrames.

### 1. 📦 Tuple `()`
- **What It Is:** An immutable (un-changeable), ordered collection of items.
- **Example:** `status_tuple = ("Valid", "Invalid", "Quarantine")`
- **When Used in Pandas:** Column names tuple in multi-index DataFrames (`df.columns`).

### 2. 📖 Dictionary `{}`
- **What It Is:** A key-value pair mapping structure.
- **Example:** `column_rename_dict = {"cust_id": "Customer_ID", "amt": "Total_Amount"}`
- **When Used in Pandas:** 
  - Renaming columns: `df.rename(columns={"cust_id": "Customer_ID"})`
  - Creating DataFrames: `df = pd.DataFrame({"Customer_ID": [101, 102], "Name": ["Alice", "Bob"]})`
  - Mapping values: `df['Status'] = df['Status_Code'].map({1: 'Active', 0: 'Inactive'})`

### 3. 📋 List `[]`
- **What It Is:** A mutable (changeable), ordered collection of items.
- **Example:** `selected_cols = ["Customer_ID", "Email", "Updated_Date"]`
- **When Used in Pandas:** Selecting specific columns: `df[selected_cols]`

---

## 🐙 SCENARIO 16: Enterprise Source Control & Git Workflows (PBIP, TMDL, Snowflake & dbt)
* **Real-World Challenge:** Managing source control, versioning, code reviews, and CI/CD deployment pipelines across Power BI reports, SQL queries, dbt models, and Snowflake scripts.

### 1. 📊 Power BI Source Control (PBIP & TMDL)
- **The Problem:** Legacy `.pbix` files are binary blobs. Git cannot merge changes or show diffs between two developers.
- **The Solution:** Save Power BI projects as **PBIP (Power BI Project format)**.
  - **TMDL (Tabular Model Definition Language):** Stores semantic model definitions (tables, relationships, DAX measures) as plain human-readable text files.
  - **Git Branching:** Developers work on feature branches (`feature/dax-revenue`), commit text TMDL changes, and merge via GitHub Pull Requests (PRs).

### 2. 🛢️ SQL & dbt Source Control
- **dbt Repository Structure:** Models are stored as SQL files in `models/marts/core/fact_sales.sql`.
- **Git CI/CD Pipeline:** Every Pull Request triggers automated dbt testing (`dbt test`) and compilation before merging into `main`.

### 3. ❄️ Snowflake Version Control & Schema Migration
- **Schema Migration Tools:** Using tools like **Schemachange** or **Liquibase** to version control Snowflake DDL scripts (`V1.1__create_tables.sql`).

---

## 🛠️ SCENARIO 17: Handling Multi-File Folder Ingestion with Inconsistent Column Headers in Power Query (M)
* **Real-World Challenge:** Ingesting multiple CSV/Excel files from a single folder where different files have different column headers (`A, B, C` vs. `G, E, F` vs. `X, Y, Z`), but represent identical schema positionally.

### 💡 The 2 Solution Approaches & When to Use Which:

#### Approach 1: Power Query Folder Combine (Sample File Transform - Recommended Best Practice)
1. **Combine Files from Folder:** Use `Folder.Files()` data connector in Power Query.
2. **Transform Sample File:** Edit the **Transform Sample File** query created automatically by Power Query.
3. **Positional Demote/Rename Header:** 
   - Remove top promoted headers step so columns become generic `Column1, Column2, Column3`.
   - Rename `Column1 -> Column A`, `Column2 -> Column B`, `Column3 -> Column C` by **column index position**.
4. **Auto-Combine All Files:** Power Query automatically applies this positional transformation schema to every file in the folder before appending them together.

#### Approach 2: Direct Combine + Filter Rows (Your Interview Answer - Perfectly Valid!)
1. **Import without Headers:** Import files skipping the auto-promote header step.
2. **Combine / Append Tables:** Append all file tables together using positional column alignment (`Column1, Column2, Column3`).
3. **Filter Header Noise Rows:** Filter out rows where `Column1 = "G"` or `Column1 = "X"`.
4. **Promote First Row:** Promote the first row (`A, B, C`) to become the unified table headers.

---

## 🛠️ SCENARIO 18: Core dbt (data build tool) Fundamentals & Snowflake Integration
* **Real-World Challenge:** Transforming raw data inside Snowflake using SQL-first dbt models, modular SQL, Jinja templating, and incremental materialization.

### 1. 🔍 What is dbt (data build tool)?
- **Core Concept:** dbt is an open-source data transformation tool that sits inside the modern data stack (T in ELT). It lets developers write modular `SELECT` statements (SQL models) and handles dependency management, testing, and documentation automatically.

### 2. 🛢️ How dbt Connects to Snowflake
- **Connection (`profiles.yml`):** Specifies Snowflake account, warehouse (`COMPUTE_WH`), database (`ANALYTICS`), schema (`PUBLIC`), and role (`TRANSFORMER`).
- **Execution:** dbt runs `dbt run` CLI command, compiling `.sql` files into native Snowflake DDL/DML queries executed directly inside Snowflake virtual warehouses.

### 3. 📄 The 3 Core dbt File Types You Need to Know:
1. **`dbt_project.yml`:** Project configuration file defining model materializations (table, view, incremental).
2. **`models/marts/dim_customers.sql`:** SQL transformation script using Jinja `ref()` functions:
   ```sql
   WITH raw_cust AS (
       SELECT * FROM {{ ref('stg_customers') }}
   )
   SELECT 
       Customer_ID,
       UPPER(Customer_Name) AS Customer_Name,
       Email
   FROM raw_cust
   QUALIFY ROW_NUMBER() OVER (PARTITION BY Customer_ID ORDER BY Updated_Date DESC) = 1;
   ```
3. **`schema.yml`:** Data Quality testing configuration:
   ```yaml
   version: 2
   models:
     - name: dim_customers
       columns:
         - name: Customer_ID
           tests:
             - unique
             - not_null
   ```

### 4. ⚡ Core dbt Commands:
- `dbt run`: Compiles and runs all SQL models inside Snowflake.
- `dbt test`: Executes data quality assertions (unique, not_null, accepted_values).
- `dbt docs generate`: Automatically builds a visual interactive data lineage graph.
