from fastapi import FastAPI
from app.api import interview_api, user_api, report_api

app = FastAPI(title="InterviewMaster AI")

app.include_router(user_api.router, prefix="/user", tags=["user"])
app.include_router(interview_api.router, prefix="/interview", tags=["interview"])
app.include_router(report_api.router, prefix="/report", tags=["report"])

@app.get("/")
def root():
    return {"message": "InterviewMaster AI - API running"}
