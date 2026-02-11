import uuid, time
from app.modules.question_generator import generate_questions
from app.modules.answer_analyzer import analyze_answer
from app.modules.scoring import compute_final_score
from app.modules.tracker import Tracker

class InterviewAgent:
    def __init__(self):
        # in-memory storage for simplicity
        self.interviews = {}
        self.tracker = Tracker()

    def start_interview(self, user_id, role='software_engineer', rounds=1):
        interview_id = str(uuid.uuid4())
        # sample resume keywords empty for now
        resume_keywords = self.tracker.get_resume_keywords(user_id) or []
        questions = generate_questions(role, resume_keywords, rounds)
        self.interviews[interview_id] = {
            "user_id": user_id,
            "role": role,
            "questions": {q['uid']: q for q in questions},
            "answers": {},
            "started_at": time.time()
        }
        return {"interview_id": interview_id, "questions": questions}

    def submit_answer(self, interview_id, question_id, answer_text):
        interview = self.interviews.get(interview_id)
        if not interview:
            return {"error":"interview not found"}
        q = interview['questions'].get(question_id)
        if not q:
            return {"error":"question not found"}
        metrics = analyze_answer(answer_text, q['text'])
        score = compute_final_score(metrics)
        interview['answers'][question_id] = {
            "question": q['text'],
            "answer": answer_text,
            "metrics": metrics,
            "score": score
        }
        # update tracker
        self.tracker.record_session(interview_id, interview)
        return {"status":"ok","metrics":metrics,"score":score}
