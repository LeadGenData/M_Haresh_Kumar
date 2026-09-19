import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build_lead_magnet_workbook(output_paths):
    wb = openpyxl.Workbook()
    
    # ----------------------------------------------------
    # Color Palette & Styles
    # ----------------------------------------------------
    NAVY_HEADER_FILL = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
    DARK_BLUE_FILL = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
    SLATE_SECTION_FILL = PatternFill(start_color="334155", end_color="334155", fill_type="solid")
    LIGHT_GRAY_FILL = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    ACCENT_GREEN_FILL = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid") # Soft green
    RECOMMENDED_FILL = PatternFill(start_color="10B981", end_color="10B981", fill_type="solid") # Emerald
    ALERT_YELLOW_FILL = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid") # Amber
    BORDER_COLOR = "CBD5E1"
    
    font_title = Font(name="Segoe UI", size=16, bold=True, color="0F172A")
    font_subtitle = Font(name="Segoe UI", size=10, italic=True, color="475569")
    font_section = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    font_col_header = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    font_data = Font(name="Segoe UI", size=10, color="1E293B")
    font_data_bold = Font(name="Segoe UI", size=10, bold=True, color="1E293B")
    font_kpi_num = Font(name="Segoe UI", size=16, bold=True, color="0F172A")
    font_kpi_label = Font(name="Segoe UI", size=9, bold=True, color="64748B")
    font_recommended = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    font_alert = Font(name="Segoe UI", size=10, bold=True, color="92400E")
    
    thin_border = Border(
        left=Side(style="thin", color=BORDER_COLOR),
        right=Side(style="thin", color=BORDER_COLOR),
        top=Side(style="thin", color=BORDER_COLOR),
        bottom=Side(style="thin", color=BORDER_COLOR)
    )
    
    double_bottom_border = Border(
        left=Side(style="thin", color=BORDER_COLOR),
        right=Side(style="thin", color=BORDER_COLOR),
        top=Side(style="thin", color=BORDER_COLOR),
        bottom=Side(style="double", color="0F172A")
    )

    # ====================================================
    # SHEET 1: EXECUTIVE SUMMARY & BID DECISION
    # ====================================================
    ws1 = wb.active
    ws1.title = "Bid_Decision_Summary"
    ws1.views.sheetView[0].showGridLines = True
    
    # Title Block
    ws1["B2"] = "COMMERCIAL CONTRACTOR 3-WAY DISTRIBUTOR & SUPPLIER QUOTE MODEL"
    ws1["B2"].font = font_title
    ws1["B3"] = "Normalized Landed Cost, Payment Term Discounts, Freight Offloading & Margin Drift Protection"
    ws1["B3"].font = font_subtitle
    
    # KPI Summary Cards (Rows 5-7)
    cards = [
        ("B", "D", "PROJECT & PACKAGE", "Rooftop HVAC RTU Package (5 Units)", "C5"),
        ("E", "G", "BID MATERIAL BUDGET", 85000.00, "F5"),
        ("H", "J", "LOWEST LANDED COST", 78420.00, "I5"),
        ("K", "M", "MARGIN PROFIT CAPTURE", 6580.00, "L5")
    ]
    
    for start_col, end_col, label, val, center_cell in cards:
        ws1.merge_cells(f"{start_col}5:{end_col}5")
        ws1.merge_cells(f"{start_col}6:{end_col}7")
        ws1[f"{start_col}5"] = label
        ws1[f"{start_col}5"].font = font_kpi_label
        ws1[f"{start_col}5"].alignment = Alignment(horizontal="center", vertical="center")
        ws1[f"{start_col}5"].fill = LIGHT_GRAY_FILL
        
        ws1[f"{start_col}6"] = val
        ws1[f"{start_col}6"].font = font_kpi_num
        ws1[f"{start_col}6"].alignment = Alignment(horizontal="center", vertical="center")
        ws1[f"{start_col}6"].fill = LIGHT_GRAY_FILL
        if isinstance(val, float):
            ws1[f"{start_col}6"].number_format = "$#,##0.00"
            
        # Border around card
        for r in range(5, 8):
            for c in range(openpyxl.utils.column_index_from_string(start_col), openpyxl.utils.column_index_from_string(end_col) + 1):
                ws1.cell(row=r, column=c).border = thin_border

    # Section Header (Row 9)
    ws1.merge_cells("B9:M9")
    ws1["B9"] = "1. EXECUTIVE 3-WAY DISTRIBUTOR LANDED COST & RISK COMPARISON"
    ws1["B9"].font = font_section
    ws1["B9"].fill = NAVY_HEADER_FILL
    ws1["B9"].alignment = Alignment(vertical="center", indent=1)
    
    # Table Column Headers (Row 10)
    headers_s1 = [
        ("B", "EVALUATION CRITERIA"),
        ("C", "ESTIMATED BUDGET"),
        ("D", "SUPPLIER A: APEX WHOLESALE"),
        ("E", "SUPPLIER B: LONESTAR DIRECT"),
        ("F", "SUPPLIER C: NATIONAL SUPPLY"),
        ("G", "VARIANCE TO BUDGET (SUPP B)"),
        ("H", "LEAD TIME RISK"),
        ("I", "PAYMENT TERMS"),
        ("J", "FREIGHT & OFFLOAD STATUS"),
        ("K", "RECOMMENDATION VERDICT"),
        ("L", "TOTAL NET SAVINGS"),
        ("M", "AUDIT NOTE")
    ]
    for col_letter, text in headers_s1:
        cell = ws1[f"{col_letter}10"]
        cell.value = text
        cell.font = font_col_header
        cell.fill = DARK_BLUE_FILL
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws1.row_dimensions[10].height = 28
    
    # Data Rows
    s1_rows = [
        ("Base Quoted Material Total", 85000.00, 79200.00, 77500.00, 81400.00, "=$C$11-E11", "Low", "Net 30", "Excluded (FOB Origin)", "REVIEW", "=C11-E11", "Apparent lowest base price"),
        ("Jobsite Freight & Liftgate", 0.00, 3800.00, 2400.00, 0.00, "=-E12", "None", "Due on Delivery", "Included in Supp C", "REQUIRED", "=-E12", "Supplier A hides $3.8k freight"),
        ("Crane Rigging & Offloading", 0.00, 1500.00, 0.00, 1200.00, "=0", "Scheduled", "Net 30", "Included in Supp B package", "SAVINGS", "=D13-E13", "Supp B includes staging rig"),
        ("Early Pay Cash Discount (2% 10 / Net 30)", 0.00, 0.00, -1480.00, -800.00, "=E14", "Immediate", "2/10 Net 30", "Applied to base", "CASH CAPTURE", "=-E14", "2% captured via 10-day pay"),
        ("Estimated Restocking / Return Fee (5%)", 0.00, 2000.00, 0.00, 1000.00, "=0", "Low", "Standard", "Waived for Supp B", "PROTECTION", "=D15-E15", "Supp B waives restock fee"),
    ]
    
    r_idx = 11
    for r in s1_rows:
        ws1[f"B{r_idx}"] = r[0]
        ws1[f"B{r_idx}"].font = font_data_bold
        ws1[f"B{r_idx}"].border = thin_border
        
        for c_idx, val in enumerate(r[1:5], start=3):
            col_l = openpyxl.utils.get_column_letter(c_idx)
            cell = ws1[f"{col_l}{r_idx}"]
            cell.value = val
            cell.font = font_data
            cell.number_format = "$#,##0.00"
            cell.alignment = Alignment(horizontal="right", vertical="center")
            cell.border = thin_border
            
        # Extra columns
        ws1[f"F{r_idx}"] = r[4] # Supplier C
        ws1[f"G{r_idx}"] = r[5] # Formula
        ws1[f"G{r_idx}"].number_format = "$#,##0.00"
        ws1[f"G{r_idx}"].font = font_data_bold
        ws1[f"G{r_idx}"].alignment = Alignment(horizontal="right", vertical="center")
        
        for c_i, v in enumerate(r[6:], start=8):
            col_l = openpyxl.utils.get_column_letter(c_i)
            cell = ws1[f"{col_l}{r_idx}"]
            cell.value = v
            cell.font = font_data
            cell.alignment = Alignment(horizontal="center", vertical="center")
            cell.border = thin_border
            if col_l == "K" and v == "SAVINGS":
                cell.fill = ACCENT_GREEN_FILL
            elif col_l == "K" and v == "REQUIRED":
                cell.fill = ALERT_YELLOW_FILL
        r_idx += 1
        
    # TOTAL TRUE LANDED COST ROW (Row 16)
    ws1[f"B{r_idx}"] = "TRUE NORMALIZED LANDED COST"
    ws1[f"B{r_idx}"].font = font_section
    ws1[f"B{r_idx}"].fill = DARK_BLUE_FILL
    ws1[f"B{r_idx}"].border = double_bottom_border
    
    ws1[f"C{r_idx}"] = "=SUM(C11:C15)"
    ws1[f"D{r_idx}"] = "=SUM(D11:D15)"
    ws1[f"E{r_idx}"] = "=SUM(E11:E15)"
    ws1[f"F{r_idx}"] = "=SUM(F11:F15)"
    ws1[f"G{r_idx}"] = "=C16-E16"
    
    for col_l in ["C", "D", "E", "F", "G"]:
        cell = ws1[f"{col_l}{r_idx}"]
        cell.font = font_section
        cell.fill = DARK_BLUE_FILL
        cell.number_format = "$#,##0.00"
        cell.alignment = Alignment(horizontal="right", vertical="center")
        cell.border = double_bottom_border
        
    ws1[f"H{r_idx}"] = "3 Weeks"
    ws1[f"I{r_idx}"] = "2/10 Net 30"
    ws1[f"J{r_idx}"] = "100% Fully Covered"
    ws1[f"K{r_idx}"] = "SELECTED: SUPP B"
    ws1[f"L{r_idx}"] = "=C16-E16"
    ws1[f"L{r_idx}"].number_format = "$#,##0.00"
    ws1[f"M{r_idx}"] = "Net savings + on-time delivery"
    
    for col_l in ["H", "I", "J", "K", "L", "M"]:
        cell = ws1[f"{col_l}{r_idx}"]
        cell.font = font_section
        cell.fill = RECOMMENDED_FILL if col_l == "K" else DARK_BLUE_FILL
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = double_bottom_border
    ws1.row_dimensions[r_idx].height = 24
    
    # CALLOUT BOX: TURNKEY CONTRACTOR OS
    r_idx += 3
    ws1.merge_cells(f"B{r_idx}:M{r_idx+3}")
    callout_cell = ws1[f"B{r_idx}"]
    callout_cell.value = (
        "💡 CONTRACTOR PROFIT AUDIT NOTE:\n"
        "Suppliers frequently quote a lower base price by stripping out liftgate delivery, crane staging, and return restocking fees.\n"
        "In this live model, Supplier A looked $1,700 cheaper on paper, but resulted in $84,500 true landed cost vs Supplier B's $78,420.\n"
        "Selecting Supplier B captured $6,580 in pure gross margin (+7.7% profit) and protected job delivery schedules.\n"
        "--------------------------------------------------------------------------------------------------------------------\n"
        "Need this connected live to your Job Costing & Invoicing? Automated Turnkey Contractor OS ($500 setup, zero monthly fees):\n"
        "Contact: M. Haresh Kumar | hareshmkumar9@gmail.com | Portfolio: leadgendata.github.io/M_Haresh_Kumar/contractor-os.html"
    )
    callout_cell.font = Font(name="Segoe UI", size=9, bold=True, color="0F172A")
    callout_cell.fill = ACCENT_GREEN_FILL
    callout_cell.alignment = Alignment(vertical="center", indent=1, wrap_text=True)
    for r in range(r_idx, r_idx + 4):
        for c in range(2, 14):
            ws1.cell(row=r, column=c).border = thin_border

    # ====================================================
    # SHEET 2: LINE-ITEM NORMALIZATION ENGINE
    # ====================================================
    ws2 = wb.create_sheet(title="Line_Item_Quote_Engine")
    ws2.views.sheetView[0].showGridLines = True
    
    ws2["B2"] = "LINE-ITEM BILL OF MATERIALS & 3-WAY DISTRIBUTOR QUOTE MATRIX"
    ws2["B2"].font = font_title
    ws2["B3"] = "Detailed Equipment, Accessories, Freight Normalization & Scope Verification"
    ws2["B3"].font = font_subtitle
    
    headers_s2 = [
        ("B", "ITEM #"),
        ("C", "MATERIAL / EQUIPMENT DESCRIPTION"),
        ("D", "SPEC / MODEL"),
        ("E", "QTY"),
        ("F", "UOM"),
        ("G", "SUPP A UNIT"),
        ("H", "SUPP A EXT"),
        ("I", "SUPP B UNIT"),
        ("J", "SUPP B EXT"),
        ("K", "SUPP C UNIT"),
        ("L", "SUPP C EXT"),
        ("M", "LOWEST EXT"),
        ("N", "BEST SUPPLIER")
    ]
    
    ws2.merge_cells("B5:N5")
    ws2["B5"] = "2. DETAILED BILL OF MATERIALS COMPARISON"
    ws2["B5"].font = font_section
    ws2["B5"].fill = NAVY_HEADER_FILL
    ws2["B5"].alignment = Alignment(vertical="center", indent=1)
    
    for col_l, text in headers_s2:
        cell = ws2[f"{col_l}6"]
        cell.value = text
        cell.font = font_col_header
        cell.fill = DARK_BLUE_FILL
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws2.row_dimensions[6].height = 26
    
    items = [
        ("01", "15-Ton Packaged Rooftop Unit (Gas/Electric)", "Carrier 48HC / Equiv", 5, "EA", 12800.00, 12400.00, 13100.00),
        ("02", "Variable Frequency Curb Adaptor Frame", "VFD-Curb-15T", 5, "EA", 950.00, 890.00, 980.00),
        ("03", "BACnet Master Digital Thermostat Controller", "BAC-DDC-500", 5, "EA", 420.00, 410.00, 440.00),
        ("04", "Heavy Gauge Condenser Hail Guard Kit", "HG-15T-PRO", 5, "EA", 380.00, 360.00, 390.00),
        ("05", "Vibration Spring Isolator Rails", "ISO-RAIL-HD", 5, "SETS", 510.00, 480.00, 520.00),
        ("06", "High-Efficiency MERV-13 Filter Bank (Spare Sets)", "M13-PKG-10", 10, "SETS", 140.00, 130.00, 150.00),
        ("07", "R-410A Refrigerant Trim Charge Cylinders (25 lb)", "R410A-CYL", 6, "CYL", 220.00, 210.00, 230.00),
        ("08", "Dedicated Flatbed Freight with Staged Liftgate", "FREIGHT-LOG", 1, "LS", 3800.00, 2400.00, 0.00),
        ("09", "Factory 5-Year Extended Compressor Warranty", "WARR-5YR-CMP", 5, "EA", 460.00, 420.00, 490.00)
    ]
    
    r_i = 7
    for item in items:
        ws2[f"B{r_i}"] = item[0]
        ws2[f"C{r_i}"] = item[1]
        ws2[f"D{r_i}"] = item[2]
        ws2[f"E{r_i}"] = item[3]
        ws2[f"F{r_i}"] = item[4]
        
        for col_l in ["B", "C", "D", "E", "F"]:
            ws2[f"{col_l}{r_i}"].font = font_data
            ws2[f"{col_l}{r_i}"].border = thin_border
            if col_l in ["B", "E", "F"]:
                ws2[f"{col_l}{r_i}"].alignment = Alignment(horizontal="center", vertical="center")
                
        # Unit Prices & Extended Formulas
        ws2[f"G{r_i}"] = item[5] # Supp A Unit
        ws2[f"H{r_i}"] = f"=E{r_i}*G{r_i}" # Supp A Ext
        ws2[f"I{r_i}"] = item[6] # Supp B Unit
        ws2[f"J{r_i}"] = f"=E{r_i}*I{r_i}" # Supp B Ext
        ws2[f"K{r_i}"] = item[7] # Supp C Unit
        ws2[f"L{r_i}"] = f"=E{r_i}*K{r_i}" # Supp C Ext
        ws2[f"M{r_i}"] = f"=MIN(H{r_i},J{r_i},L{r_i})" # Lowest Ext
        ws2[f"N{r_i}"] = f'=IF(M{r_i}=J{r_i},"Supplier B",IF(M{r_i}=H{r_i},"Supplier A","Supplier C"))'
        
        for col_l in ["G", "H", "I", "J", "K", "L", "M"]:
            cell = ws2[f"{col_l}{r_i}"]
            cell.font = font_data
            cell.number_format = "$#,##0.00"
            cell.alignment = Alignment(horizontal="right", vertical="center")
            cell.border = thin_border
            
        ws2[f"N{r_i}"].font = font_data_bold
        ws2[f"N{r_i}"].alignment = Alignment(horizontal="center", vertical="center")
        ws2[f"N{r_i}"].border = thin_border
        if item[0] == "08": # Freight callout
            ws2[f"L{r_i}"].fill = ALERT_YELLOW_FILL # Supp C shows 0 freight because it rolled into unit price
        r_i += 1
        
    # TOTAL ROW
    ws2[f"B{r_i}"] = "TOTAL"
    ws2.merge_cells(f"B{r_i}:F{r_i}")
    ws2[f"B{r_i}"].font = font_section
    ws2[f"B{r_i}"].fill = DARK_BLUE_FILL
    ws2[f"B{r_i}"].alignment = Alignment(horizontal="center", vertical="center")
    ws2[f"B{r_i}"].border = double_bottom_border
    
    ws2[f"H{r_i}"] = f"=SUM(H7:H{r_i-1})"
    ws2[f"J{r_i}"] = f"=SUM(J7:J{r_i-1})"
    ws2[f"L{r_i}"] = f"=SUM(L7:L{r_i-1})"
    ws2[f"M{r_i}"] = f"=SUM(M7:M{r_i-1})"
    ws2[f"N{r_i}"] = "SUPPLIER B"
    
    for col_l in ["G", "H", "I", "J", "K", "L", "M"]:
        cell = ws2[f"{col_l}{r_i}"]
        cell.font = font_section
        cell.fill = DARK_BLUE_FILL
        if col_l in ["H", "J", "L", "M"]:
            cell.number_format = "$#,##0.00"
        cell.alignment = Alignment(horizontal="right", vertical="center")
        cell.border = double_bottom_border
        
    ws2[f"N{r_i}"].font = font_recommended
    ws2[f"N{r_i}"].fill = RECOMMENDED_FILL
    ws2[f"N{r_i}"].alignment = Alignment(horizontal="center", vertical="center")
    ws2[f"N{r_i}"].border = double_bottom_border

    # ====================================================
    # SHEET 3: MARGIN DRIFT & CASH FLOW SENSITIVITY
    # ====================================================
    ws3 = wb.create_sheet(title="Margin_Impact_Analysis")
    ws3.views.sheetView[0].showGridLines = True
    
    ws3["B2"] = "CONTRACT GROSS MARGIN DRIFT & CASH FLOW SENSITIVITY"
    ws3["B2"].font = font_title
    ws3["B3"] = "How Supplier Normalization Protects $6,500+ Profit on a $140,000 Commercial Contract"
    ws3["B3"].font = font_subtitle
    
    ws3.merge_cells("B5:H5")
    ws3["B5"] = "3. JOB FINANCIAL SUMMARY & SENSITIVITY TABLE"
    ws3["B5"].font = font_section
    ws3["B5"].fill = NAVY_HEADER_FILL
    ws3["B5"].alignment = Alignment(vertical="center", indent=1)
    
    headers_s3 = [
        ("B", "FINANCIAL METRIC"),
        ("C", "TAKEOFF ESTIMATE"),
        ("D", "WITH SUPPLIER A (UNPACKAGED)"),
        ("E", "WITH SUPPLIER B (NORMALIZED)"),
        ("F", "WITH SUPPLIER C (NATIONAL)"),
        ("G", "SUPPLIER B GAIN / LOSS"),
        ("H", "STRATEGIC IMPACT")
    ]
    for col_l, text in headers_s3:
        cell = ws3[f"{col_l}6"]
        cell.value = text
        cell.font = font_col_header
        cell.fill = DARK_BLUE_FILL
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws3.row_dimensions[6].height = 26
    
    s3_data = [
        ("Total Prime Contract Value", 140000.00, 140000.00, 140000.00, 140000.00, 0.00, "Fixed Client Billing"),
        ("Direct Jobsite Labor", 22000.00, 22000.00, 22000.00, 22000.00, 0.00, "Standard 2-Week Crew"),
        ("Equipment Rigging & Subcontractor", 6500.00, 8000.00, 6500.00, 7700.00, 1500.00, "Supp B covers staging rig"),
        ("Material & Equipment Landed Cost", 85000.00, 84500.00, 78420.00, 81400.00, 6580.00, "Supp B 2% discount captured"),
        ("Total Direct Job Cost", "=C8+C9+C10", "=D8+D9+D10", "=E8+E9+E10", "=F8+F9+F10", "=D11-E11", "Total landed cost"),
        ("Gross Margin Profit Dollars", "=C7-C11", "=D7-D11", "=E7-E11", "=F7-F11", "=E12-D12", "NET CASH CAPTURE"),
        ("Gross Margin Percentage", "=C12/C7", "=D12/D7", "=E12/E7", "=F12/F7", "=E13-D13", "PERCENTAGE GAIN")
    ]
    
    r_idx = 7
    for row in s3_data:
        ws3[f"B{r_idx}"] = row[0]
        ws3[f"B{r_idx}"].font = font_data_bold
        ws3[f"B{r_idx}"].border = thin_border
        
        for c_i, v in enumerate(row[1:6], start=3):
            col_l = openpyxl.utils.get_column_letter(c_i)
            cell = ws3[f"{col_l}{r_idx}"]
            cell.value = v
            cell.font = font_data_bold if r_idx in [11, 12, 13] else font_data
            if r_idx == 13: # Percentage
                cell.number_format = "0.0%"
            else:
                cell.number_format = "$#,##0.00"
            cell.alignment = Alignment(horizontal="right", vertical="center")
            cell.border = thin_border
            if r_idx == 12 and col_l == "E":
                cell.fill = ACCENT_GREEN_FILL
            elif r_idx == 13 and col_l == "E":
                cell.fill = ACCENT_GREEN_FILL
                
        ws3[f"H{r_idx}"] = row[6]
        ws3[f"H{r_idx}"].font = font_data
        ws3[f"H{r_idx}"].alignment = Alignment(horizontal="center", vertical="center")
        ws3[f"H{r_idx}"].border = thin_border
        r_idx += 1

    # ====================================================
    # Auto-Fit Column Widths for All Sheets
    # ====================================================
    for sheet in wb.worksheets:
        for col in sheet.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                if cell.row < 4: # Skip title
                    continue
                val_str = str(cell.value or "")
                if len(val_str) > max_len:
                    max_len = len(val_str)
            sheet.column_dimensions[col_letter].width = max(max_len + 3, 12)
        sheet.column_dimensions["A"].width = 4
        sheet.column_dimensions["B"].width = 38
        if sheet.title == "Line_Item_Quote_Engine":
            sheet.column_dimensions["C"].width = 44
            sheet.column_dimensions["D"].width = 24

    # Save to targets
    for p in output_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        wb.save(p)
        print(f"Saved: {p}")

if __name__ == "__main__":
    local_path = r"e:\BDL_PRO_Claude\scratch\single_portfolio_repo\templates\Subcontractor_&_Supplier_3_Way_Quote_Comparison_Model.xlsx"
    drive_path = r"H:\My Drive\1_Career_&_Study_Sync\Subcontractor_&_Supplier_3_Way_Quote_Comparison_Model.xlsx"
    build_lead_magnet_workbook([local_path, drive_path])
