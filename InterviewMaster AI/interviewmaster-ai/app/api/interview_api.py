from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.modules.interview_agent import InterviewAgent

router = APIRouter()
agent = InterviewAgent()

class StartRequest(BaseModel):
    user_id: str
    role: str = "software_engineer"
    rounds: int = 1

class AnswerPayload(BaseModel):
    user_id: str
    interview_id: str
    question_id: str
    answer: str

@router.post("/start")
def start_interview(req: StartRequest):
    interview = agent.start_interview(req.user_id, req.role, req.rounds)
    return interview

@router.post("/answer")
def submit_answer(payload: AnswerPayload):
    res = agent.submit_answer(payload.interview_id, payload.question_id, payload.answer)
    return res
