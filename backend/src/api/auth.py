from fastapi import APIRouter
from models.user import User

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/add")
async def add_user(user : User):
    #add new user
    return {}

@router.post("/{user_id}/show")
async def show_user_detail():
    #show user with there assets
    return {}
