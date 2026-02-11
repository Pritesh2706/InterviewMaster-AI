# Simple tracker storing resume keywords and interview history
class Tracker:
    def __init__(self):
        self.data = {}
    def record_resume(self, user_id, keywords):
        self.data.setdefault(user_id,{})
        self.data[user_id]['resume_keywords'] = keywords
    def get_resume_keywords(self, user_id):
        return self.data.get(user_id,{}).get('resume_keywords',[])
    def record_session(self, interview_id, interview_obj):
        # store last session under data
        user_id = interview_obj.get('user_id')
        self.data.setdefault(user_id,{}).setdefault('sessions',{})
        self.data[user_id]['sessions'][interview_id]=interview_obj
