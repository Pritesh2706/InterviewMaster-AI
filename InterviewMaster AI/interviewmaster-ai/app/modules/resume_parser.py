import re
def parse_resume_text(text: str):
    # Very simple keyword extractor: skills = capitalized words or tech words
    keywords = set()
    tech_terms = ['python','sql','java','c++','spark','pyspark','aws','docker','kubernetes','ml','nlp']
    text_lower = text.lower()
    for term in tech_terms:
        if term in text_lower:
            keywords.add(term)
    # also grab words following 'Skills:' or 'Technologies:'
    m = re.search(r'(skills|technologies):\s*(.*)', text_lower)
    if m:
        parts = re.split('[,;\n]', m.group(2))
        for p in parts:
            kw = p.strip()
            if kw:
                keywords.add(kw)
    return list(keywords)
