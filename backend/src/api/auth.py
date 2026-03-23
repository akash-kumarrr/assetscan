from fastapi import APIRouter, HTTPException, status
from models.user import User
from google.cloud import firestore
from db import db  # Cleaned up import

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/add", status_code=status.HTTP_201_CREATED)
def add_user(user: User):
    try:
        user_data = user.model_dump()
        # Use SERVER_TIMESTAMP for indexing and consistency
        user_data['created_at'] = firestore.SERVER_TIMESTAMP

        # Blocking call handled by FastAPI's threadpool
        db.collection("users").document(user.id).set(user_data)
        
        return {
            'message': 'User added successfully',
            'id': user.id
        }
    except Exception as e:
        # Log 'e' internally, don't expose raw error to user in prod
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{user_id}/show")
def show_user_detail(user_id: str):
    try:
        # 1. Fetch User Document
        user_ref = db.collection("users").document(user_id).get()
        
        if not user_ref.exists:
            raise HTTPException(status_code=404, detail="User not found")
        
        user_data = user_ref.to_dict()

        # 2. Fetch User's Assets (Assuming a top-level collection with a user_id field)
        # Production tip: Ensure 'user_id' is indexed in Firestore
        assets_query = db.collection("assets").where("user_id", "==", user_id).stream()
        assets = [doc.to_dict() for doc in assets_query]

        return {
            "user": user_data,
            "assets": assets
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not retrieve user details")