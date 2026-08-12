# 📅 MASTER GUIDE: POWER BI DAX DATE TABLES & TABLE TRANSFORMATIONS
### Complete Technical Reference for Enterprise Modeling & Interviews

---

## 📑 1. WHY CUSTOM DATE TABLES ARE MANDATORY IN ENTERPRISE BI
In enterprise Power BI modeling, **never rely on Power BI's default "Auto Date/Time" setting**. 
* **The Problem:** Auto Date/Time creates a hidden date hierarchy table for every single date column in your dataset, causing massive VertiPaq memory bloat.
* **The Solution:** Disable "Auto Date/Time" in Options $\rightarrow$ Data Load, and create **one dedicated, marked Date Dimension table (`Dim_Date`)**.

---

## 🛠️ 2. COMPLETE DAX DATE TABLE USING VARIABLES (`VAR` / `RETURN`)

```dax
Dim_Date = 
-- Step 1: Capture Minimum and Maximum Years dynamically from Fact Table
VAR MinYear = YEAR(MIN(Fact_Sales[Order_Date]))
VAR MaxYear = YEAR(MAX(Fact_Sales[Order_Date]))

-- Step 2: Create continuous date range from Jan 1 of MinYear to Dec 31 of MaxYear
VAR BaseCalendar = CALENDAR(DATE(MinYear, 1, 1), DATE(MaxYear, 12, 31))

-- Step 3: Return expanded Date Dimension table with custom attributes
RETURN
    ADDCOLUMNS(
        BaseCalendar,
        "Year", YEAR([Date]),
        "Month_Number", MONTH([Date]),
        "Month_Name", FORMAT([Date], "MMM"),
        "Month_Year", FORMAT([Date], "MMM YYYY"),
        "Year_Month_Sort", YEAR([Date]) * 100 + MONTH([Date]),
        "Quarter", "Q" & FORMAT([Date], "Q"),
        "Quarter_Year", "Q" & FORMAT([Date], "Q") & " " & YEAR([Date]),
        "Day_Number", DAY([Date]),
        "Day_of_Week", FORMAT([Date], "DDD"),
        "Day_of_Week_Number", WEEKDAY([Date], 2), -- 1 = Monday, 7 = Sunday
        "Is_Weekend", IF(WEEKDAY([Date], 2) >= 6, "Weekend", "Weekday")
    )
```

---

## 🔍 3. CORE DAX TABLE FUNCTIONS EXPLAINED (PLAIN ENGLISH)

### 1. `VAR` & `RETURN`
* **Purpose:** Stores temporary scalar values or table expressions in memory.
* **Why Use It:** Improves DAX performance (evaluates expression once instead of recalculating multiple times) and makes code clean and readable.

### 2. `CALENDAR()` vs `CALENDARAUTO()`
* **`CALENDAR(StartDate, EndDate)`:** Generates a single column of continuous dates between specified start and end dates.
* **`CALENDARAUTO([FiscalYearEndMonth])`:** Automatically inspects the entire data model, finds the earliest and latest dates, and creates a continuous date table.

### 3. `ADDCOLUMNS(Table, "Name1", Expression1, ...)`
* **Purpose:** Takes an existing table (e.g. `BaseCalendar`) and appends new calculated columns to it.

### 4. `FILTER(Table, Condition)`
* **Purpose:** Scans a table row-by-row and returns a filtered sub-table matching the condition.
* **Example (Excluding Weekends from Date Table):**
  ```dax
  Dim_Workdays = 
  FILTER(
      Dim_Date,
      Dim_Date[Is_Weekend] = "Weekday"
  )
  ```

### 5. `SUMMARIZE(Table, GroupBy_Column1, "NewCol", AggExpression)`
* **Purpose:** Groups data similar to SQL `GROUP BY` and returns an aggregated summary table.
* **Example:**
  ```dax
  Customer_Sales_Summary = 
  SUMMARIZE(
      Fact_Sales,
      Fact_Sales[Customer_ID],
      "Total_Sales", SUM(Fact_Sales[Amount])
  )
  ```

### 6. `CALCULATETABLE(Table, Filter1, Filter2)`
* **Purpose:** Evaluates a table expression under a modified filter context (similar to `CALCULATE` for tables).

---

## ⏱️ 4. TIME INTELLIGENCE FUNCTIONS (REQUIRES MARKED DATE TABLE)

Once `Dim_Date` is marked as a Date Table in Power BI, you can use these core Time Intelligence measures:

```dax
-- Year-to-Date (YTD) Revenue
YTD_Revenue = CALCULATE(SUM(Fact_Sales[Amount]), DATESYTD(Dim_Date[Date]))

-- Previous Year Revenue (Same Period Last Year)
PY_Revenue = CALCULATE(SUM(Fact_Sales[Amount]), SAMEPERIODLASTYEAR(Dim_Date[Date]))

-- Year-over-Year (YoY) Growth %
YoY_Growth_% = 
VAR CurrentSales = [YTD_Revenue]
VAR PriorSales = [PY_Revenue]
RETURN
    DIVIDE(CurrentSales - PriorSales, PriorSales, 0)
```

---

*Artifact Path:* [master_dax_date_tables_guide.md](file:///C:/Users/hi/Desktop/Antigavtty%20Notes/Master_DAX_Date_Tables_Guide.md)
