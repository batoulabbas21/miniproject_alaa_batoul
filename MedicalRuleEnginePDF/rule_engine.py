import re

def evaluate_rules(text):
    alerts = []

    # Rule 1: Diabetes – HbA1c ≥ 6.5%
    match = re.search(r"HbA1c[:\s]*([0-9.]+)%", text, re.I)
    if match and float(match.group(1)) >= 6.5:
        alerts.append("Diabetes Alert: HbA1c ≥ 6.5%")

    # Rule 2: Hypertension – Systolic ≥ 180 or Diastolic ≥ 110
    systolic_match = re.search(r"Systolic[:\s]*([0-9]+)", text, re.I)
    diastolic_match = re.search(r"Diastolic[:\s]*([0-9]+)", text, re.I)
    if systolic_match and int(systolic_match.group(1)) >= 180:
        alerts.append("Hypertension Alert: Systolic ≥ 180 mmHg")
    if diastolic_match and int(diastolic_match.group(1)) >= 110:
        alerts.append("Hypertension Alert: Diastolic ≥ 110 mmHg")

    # Also detect if it's written as BP: 190/110
    bp_match = re.search(r"BP[:\s]*(\d{2,3})/(\d{2,3})", text, re.I)
    if bp_match:
        sys, dia = int(bp_match.group(1)), int(bp_match.group(2))
        if sys >= 180:
            alerts.append("Hypertension Alert: Systolic ≥ 180 mmHg")
        if dia >= 110:
            alerts.append("Hypertension Alert: Diastolic ≥ 110 mmHg")

    # Rule 3: High LDL – LDL ≥ 160
    match = re.search(r"LDL Cholesterol[:\s]*([0-9.]+)", text, re.I)
    if match and float(match.group(1)) >= 160:
        alerts.append("High LDL Cholesterol Alert: LDL ≥ 160 mg/dL")

    # Rule 4: Sepsis – Temp ≥ 38°C, WBC ≥ 12,000, BP systolic ≤ 100
    temp_match = re.search(r"Temperature[:\s]*([0-9.]+)", text, re.I)
    wbc_match = re.search(r"WBC[^0-9]*([0-9,]+)", text, re.I)
    bp_match = re.search(r"Blood Pressure[:\s]*([0-9]+)/", text, re.I)
    if temp_match and wbc_match and bp_match:
        temp = float(temp_match.group(1))
        wbc = int(wbc_match.group(1).replace(",", ""))
        systolic = int(bp_match.group(1))
        if temp >= 38 and wbc >= 12000 and systolic <= 100:
            alerts.append("Sepsis Alert: Temp ≥ 38°C, WBC ≥ 12k, BP ≤ 100")

    # Rule 5: CKD – GFR < 60 or Creatinine > 1.5
    gfr_match = re.search(r"GFR[:\s]*([0-9.]+)", text, re.I)
    if gfr_match and float(gfr_match.group(1)) < 60:
        alerts.append("CKD Alert: GFR < 60 mL/min/1.73m²")

    creat_match = re.search(r"Creatinine[:\s]*([0-9.]+)", text, re.I)
    if creat_match and float(creat_match.group(1)) > 1.5:
        alerts.append("CKD Alert: Creatinine > 1.5 mg/dL")

    return alerts
