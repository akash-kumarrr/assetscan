from fastapi import APIRouter
from models.asset import Asset

router = APIRouter(prefix="/assets", tags=["asset"])

@router.post("/add")
async def add_asset(asset : Asset):
    return {
        'message' : 'Asset added successfully',
        'name' : str(asset.name),
        'model' : str(asset.model),
        'serial' : str(asset.serial_number)
    }

@router.post("/{asset_id}/show")
async def show_details(asset_id):
    return {}

