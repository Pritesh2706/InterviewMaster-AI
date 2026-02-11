from fastapi import APIRouter, HTTPException
from app.modules.report_maker import ReportMaker

router = APIRouter()
maker = ReportMaker()

@router.get("/{interview_id}")
def get_report(interview_id: str):
    path = maker.generate_markdown_report(interview_id)
    if not path:
        raise HTTPException(status_code=404, detail="Interview not found")
    return {"report_path": path}
