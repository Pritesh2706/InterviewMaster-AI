from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict
from app.modules.user_profile import UserProfileManager

router = APIRouter()
manager = UserProfileManager()

class UserCreate(BaseModel):
    user_id: str
    name: str
    email: str

@router.post("/create")
def create_user(payload: UserCreate):
    if manager.get(payload.user_id):
        raise HTTPException(status_code=400, detail="User already exists")
    manager.create(payload.user_id, payload.name, payload.email)
    return {"status":"ok","user_id":payload.user_id}
