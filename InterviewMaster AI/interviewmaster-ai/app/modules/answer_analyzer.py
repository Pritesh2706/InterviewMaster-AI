import re
def analyze_answer(answer: str, question_text: str):
    # Very simple heuristics:
    # length score, keyword match score, structure score
    length = len(answer.split())
    length_score = min(10, max(0, length/10))  # 0-10
    keywords = []
    for w in re.findall(r"\w+", question_text.lower()):
        if len(w)>3:
            keywords.append(w)
    match = 0
    for kw in keywords:
        if kw in answer.lower():
            match += 1
    match_score = min(10, match)
    structure_score = 10 if answer.strip().endswith('.') else 7
    # normalize to 0-10
    return {
        "length_score": round(length_score,2),
        "keyword_match": match_score,
        "structure_score": structure_score,
        "final_estimate": round((length_score*0.4 + match_score*0.4 + structure_score*0.2),2)
    }
