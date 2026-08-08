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
