import os
from app.modules.interview_agent import InterviewAgent

# NOTE: In-memory agent; in production link to DB
AGENT = InterviewAgent()

class ReportMaker:
    def __init__(self, out_dir='/mnt/data/interview_reports'):
        self.out_dir = out_dir
        os.makedirs(out_dir, exist_ok=True)

    def generate_markdown_report(self, interview_id: str):
        # find interview in agent storage
        interview = AGENT.interviews.get(interview_id)
        if not interview:
            return None
        md = []
        md.append(f"# Interview Report: {interview_id}\n")
        md.append(f"Role: {interview.get('role')}\n")
        total = 0
        count = 0
        for qid, ans in interview['answers'].items():
            md.append(f"## Q: {ans['question']}\n")
            md.append(f"**A:** {ans['answer']}\n")
            md.append(f"**Score:** {ans['score']}\n")
            md.append(f"**Metrics:** {ans['metrics']}\n")
            total += ans['score']
            count += 1
        overall = round(total/count,2) if count else 0
        md.append(f"\n**Overall score:** {overall}\n")
        path = os.path.join(self.out_dir, f"report_{interview_id}.md")
        with open(path,'w') as f:
            f.write('\n'.join(md))
        return path
