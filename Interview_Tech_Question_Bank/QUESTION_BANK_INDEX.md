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
