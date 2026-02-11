# Simple in-memory user profile manager
class UserProfileManager:
    def __init__(self):
        self.users = {}

    def create(self, user_id, name, email):
        self.users[user_id] = {"name": name, "email": email}

    def get(self, user_id):
        return self.users.get(user_id)
