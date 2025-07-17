from fpdf import FPDF
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.model.report import Report  # Make sure this is accessible
from backend.database import SessionLocal  # Or manually define your engine if needed

def export_report_to_pdf(report):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Report: {report.filename}", ln=True, align='L')
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt=f"Summary:\n{report.summary}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt=f"Risks:\n{report.risks}")

    filename = f"exported_reports/{report.filename.replace('.txt', '').replace('.pdf', '')}_summary.pdf"
    pdf.output(filename)
    print(f"✅ Exported: {filename}")

def export_all_reports():
    session = SessionLocal()
    reports = session.query(Report).all()
    session.close()

    import os
    os.makedirs("exported_reports", exist_ok=True)

    for report in reports:
        export_report_to_pdf(report)
        
if __name__ == "__main__":
    export_all_reports()
