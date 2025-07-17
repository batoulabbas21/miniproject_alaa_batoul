from fastapi import APIRouter, File, UploadFile, HTTPException
from backend.services.pdf_utils import extract_text_from_pdf
from backend.services.summarize import summarize_text
from backend.services.ner import extract_entities
from backend.services.flagger import flag_risks
from backend.database import SessionLocal
from backend.model.report import Report
from fastapi.responses import FileResponse

router = APIRouter(prefix="/analyze", tags=["analyze"])

@router.post("/")
async def analyze_report(file: UploadFile = File(...)):
    try:
        data = await file.read()
        print(f"✅ Received file: {file.filename}")
        if file.filename.lower().endswith(".pdf"):
            text = extract_text_from_pdf(data)
        else:
            text = data.decode("utf-8")
        print("✅ Text extracted:\n", text[:300])
    except Exception as e:
        print("❌ File processing error:", e)
        raise HTTPException(status_code=400, detail=f"File processing failed: {str(e)}")

    try:
        summary = summarize_text(text)
        print("✅ Summary generated:\n", summary[:200])
        entities = extract_entities(text)
        print("✅ Entities extracted:", entities)
        flags = flag_risks(text)
        print("✅ Risk flags:", flags)
    except Exception as e:
        print("❌ Model pipeline error:", e)
        raise HTTPException(status_code=500, detail=f"Model pipeline error: {str(e)}")

    try:
        db = SessionLocal()
        report = Report(
            filename=file.filename,
            summary=summary,
            risks=", ".join(flags)
        )
        db.add(report)
        db.commit()
        db.refresh(report)
        db.close()
        print("✅ Report saved to database")
    except Exception as e:
        print("❌ Database error:", e)
        raise HTTPException(status_code=500, detail="Database error")

    return {
        "summary": summary,
        "entities": entities,
        "flags": flags
    }

@router.get("/reports/")
def get_reports():
    db = SessionLocal()
    reports = db.query(Report).all()
    db.close()
    return reports

@router.get("/reports/{report_id}")
def get_report(report_id: int):
    db = SessionLocal()
    report = db.query(Report).filter(Report.id == report_id).first()
    db.close()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return {
        "id": report.id,
        "filename": report.filename,
        "summary": report.summary,
        "risks": report.risks
    }

@router.get("/reports/{report_id}/export", tags=["analyze"])
def export_single_report(report_id: int):
    db = SessionLocal()
    report = db.query(Report).filter(Report.id == report_id).first()
    db.close()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    from export_reports import export_report_to_pdf
    export_report_to_pdf(report)
    filename = f"exported_reports/{report.filename.replace('.txt', '').replace('.pdf', '')}_summary.pdf"
    return FileResponse(filename, media_type='application/pdf', filename=filename)


