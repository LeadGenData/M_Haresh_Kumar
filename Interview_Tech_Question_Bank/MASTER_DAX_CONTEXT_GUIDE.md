# ⚡ MASTER GUIDE: DAX ROW CONTEXT vs. FILTER CONTEXT & CONTEXT TRANSITION
### The Complete Technical Breakdown for Power BI Architecture & Interviews

---

## 1. 🔄 ROW CONTEXT (ROW-BY-ROW ITERATION)

### 📌 Definition:
Row Context means evaluating an expression **one single row at a time**. 

### 💡 Key Characteristics:
* **Where It Exists:** 
  1. **Calculated Columns:** Power BI automatically creates a Row Context when evaluating a calculated column.
  2. **Iterating Functions (`SUMX`, `AVERAGEX`, `FILTER`):** Iterators loop through a table row-by-row.
* **Critical Rule:** **Row Context does NOT automatically filter other tables through relationships!** It only knows about the current row in the current table.

### 📝 Code Example:
```dax
-- Calculated Column in Fact_Sales
Line_Item_Total = Fact_Sales[Quantity] * Fact_Sales[Unit_Price] 
-- Evaluated row-by-row for every single record in Fact_Sales
```

---

## 2. 🎯 FILTER CONTEXT (THE ACTIVE FILTER ENVIRONMENT)

### 📌 Definition:
Filter Context is the **active subset of data** remaining in the data model after all slicers, visual coordinates, and `CALCULATE` filters are applied.

### 💡 Key Characteristics:
* **Where It Comes From:**
  1. **Report Visual Slicers & Filters Pane.**
  2. **Row & Column Headers in a Matrix / Bar Chart.**
  3. **Explicit DAX Filters** inside `CALCULATE(Measure, Dim_Customer[Region] = "India")`.
* **Critical Rule:** **Filter Context DOES filter other tables!** Filters flow across active relationships from Dimension tables ($1$) to Fact tables ($M$).

### 📝 Code Example:
```dax
-- Measure evaluated under Filter Context
India_Sales = 
CALCULATE(
    SUM(Fact_Sales[Amount]),
    Dim_Customer[Region] = "India" -- Overrides/Applies Filter Context
)
```

---

## 3. ⚡ CONTEXT TRANSITION (ROW CONTEXT $\rightarrow$ FILTER CONTEXT)

### 📌 Definition:
Context Transition is the process where **a Row Context is converted into an equivalent Filter Context**.

### 💡 How It Happens:
* **The Magic Trigger:** **`CALCULATE()`** is the ONLY function that performs Context Transition!
* When `CALCULATE()` is executed inside a Row Context (like a calculated column or `SUMX`), it takes the values of the current row and turns them into active filters on the data model!

### 📝 Code Example:
```dax
-- Calling a measure inside a calculated column triggers Context Transition automatically!
Total_Customer_Sales_Col = [Total_Sales] 
-- Internally evaluated as: CALCULATE([Total_Sales])
-- Transforms the current Customer_ID row into an active filter!
```

---

## 📊 4. COMPARISON MATRIX FOR INTERVIEWS

```
┌──────────────────────────────────────────────────────────────────────────┐
│                   ROW CONTEXT vs. FILTER CONTEXT MATRIX                  │
├──────────────────────────┬──────────────────────┬────────────────────────┤
│ PARAMETER                │ ROW CONTEXT          │ FILTER CONTEXT         │
├──────────────────────────┼──────────────────────┼────────────────────────┤
│ What it does             │ Iterates row-by-row  │ Filters entire dataset │
├──────────────────────────┼──────────────────────┼────────────────────────┤
│ Created by               │ Calculated Columns,  │ Slicers, Visual Rows,  │
│                          │ `SUMX`, `FILTER`     │ `CALCULATE()`          │
├──────────────────────────┼──────────────────────┼────────────────────────┤
│ Filters across           │ ❌ NO                │ ✅ YES                 │
│ relationships?           │ (Unless `CALCULATE`  │ (Flows 1 to Many)      │
│                          │  is used)            │                        │
└──────────────────────────┴──────────────────────┴────────────────────────┘
```

---

*Artifact Path:* [master_dax_context_guide.md](file:///C:/Users/hi/Desktop/Antigavtty%20Notes/Master_DAX_Context_Guide.md)
