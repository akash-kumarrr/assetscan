from fastapi import APIRouter, HTTPException
from models.asset import Asset
from google.cloud import firestore
from db import db 

router = APIRouter(prefix="/assets", tags=["asset"])

@router.post("/add")
async def add_asset(asset : Asset):
    try:
        asset_data = asset.model_dump()
        asset_data["created_on"] = firestore.SERVER_TIMESTAMP
        db.collection("assets").document(asset.id).set(asset_data)
        return {
            "message" : "Asset added successfully",
            "name" : asset.name,
        }
    except HTTPException:
        raise
    except Exception as e :
        raise HTTPException(status_code=500, detial=str(e))



@router.post("/{asset_id}/show")
async def show_details(asset_id):
    return {}

