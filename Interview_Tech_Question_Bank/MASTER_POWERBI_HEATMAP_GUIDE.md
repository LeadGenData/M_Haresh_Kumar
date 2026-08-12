# 🗺️ MASTER GUIDE: CREATING CUSTOM HOUR TABLES & MATRIX HEAT MAPS IN POWER BI
### Operational Heat Map Analytics for SLA Capacity Planning & Shift Rostering

---

## 🛠️ 1. CREATING A DAX CUSTOM HOUR DIMENSION TABLE (`Dim_Hour`)

Instead of extracting hour integers ad-hoc, we build a dedicated 24-hour dimension table using `GENERATESERIES(0, 23, 1)` and `ADDCOLUMNS()`.

```dax
Dim_Hour = 
ADDCOLUMNS(
    GENERATESERIES(0, 23, 1),
    "Hour_Number", [Value],
    "Hour_Label", FORMAT(TIME([Value], 0, 0), "hh:00 AM/PM"), -- e.g. "09:00 AM", "10:00 AM"
    "Time_Slot", 
        SWITCH(
            TRUE(),
            [Value] >= 6 && [Value] < 12, "Morning Peak",
            [Value] >= 12 && [Value] < 17, "Afternoon Shift",
            [Value] >= 17 && [Value] < 22, "Evening Shift",
            "Night Shift"
        )
)
```

---

## 📊 2. HOW TO BUILD THE MATRIX HEAT MAP VISUAL IN POWER BI

### Step-by-Step Configuration:

1. **Select Visual:** Add a **Matrix Visual** to the report canvas.
2. **Rows Field:** Drag `Dim_Date[Day_of_Week]` (Monday to Sunday).
   * *Pro Tip:* Sort `Day_of_Week` by `Day_of_Week_Number` (1 to 7) so days appear in order!
3. **Columns Field:** Drag `Dim_Hour[Hour_Label]` (00:00 to 23:00).
   * *Pro Tip:* Sort `Hour_Label` by `Hour_Number` (0 to 23) so hours sequence from 12:00 AM to 11:00 PM!
4. **Values Field:** Drag `[Total_Ticket_Volume]` or `[Avg_Response_Time_Sec]`.
5. **Enable Conditional Formatting (The Heat Map Effect):**
   * Right-click `[Total_Ticket_Volume]` under Values $\rightarrow$ **Conditional Formatting** $\rightarrow$ **Background Color**.
   * Select **Format Style: Gradient**.
   * Lowest Value: Neutral Light Blue (`#E3F2FD`).
   * Highest Value: Coral / Dark Red (`#D32F2F`).

---

## 🧠 3. WHY LEADERSHIP LOVES MATRIX HEAT MAPS (OPERATIONAL VALUE)

```
┌──────────────────────────────────────────────────────────────────────────┐
│                   MATRIX HEAT MAP OPERATIONAL VALUE                      │
├──────────────────────────┬──────────────────────────────────────────────┤
│ BUSINESS PROBLEM         │ HEAT MAP SOLUTION                            │
├──────────────────────────┼──────────────────────────────────────────────┤
│ Unidentified Ticket      │ Visually highlights dark red "hotspots"      │
│ Spikes & SLA Breaches    │ (e.g. Hour 10: 10:00 AM Local Peak) across   │
│                          │ multi-country shift operations.              │
├──────────────────────────┼──────────────────────────────────────────────┤
│ Sub-Optimal Staff        │ Operations Managers can re-allocate analyst  │
│ Roster Allocation        │ shifts directly to peak hours, eliminating   │
│                          │ queue bottlenecks before SLAs break!         │
└──────────────────────────┴──────────────────────────────────────────────┘
```

---

*Artifact Path:* [master_powerbi_heatmap_guide.md](file:///C:/Users/hi/Desktop/Antigavtty%20Notes/Master_PowerBI_Heatmap_Guide.md)
