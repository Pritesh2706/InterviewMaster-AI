import uuid
SAMPLE_BANK = {
    "software_engineer": [
        {"id":"q1","text":"Explain the differences between List and Tuple in Python."},
        {"id":"q2","text":"How does memory management work in Python?"},
        {"id":"q3","text":"Describe a project you built using SQL and how you optimized queries."}
    ],
    "data_engineer": [
        {"id":"q1","text":"What is partitioning and why is it useful in data processing?"},
        {"id":"q2","text":"Explain the difference between batch and stream processing."}
    ]
}

def generate_questions(role: str, resume_keywords: list, rounds: int =1):
    bank = SAMPLE_BANK.get(role, SAMPLE_BANK['software_engineer'])
    questions = []
    # pick questions and add resume-based ones
    for i in range(rounds):
        for q in bank:
            qcopy = q.copy()
            qcopy["uid"] = str(uuid.uuid4())
            questions.append(qcopy)
    # create resume-based prompts
    for kw in resume_keywords[:3]:
        questions.append({"id":"resume_"+kw,"uid":str(uuid.uuid4()), "text":f'Explain your experience with {kw} in detail.'})
    return questions
