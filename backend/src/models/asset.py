from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Status(str, Enum):
    AVAILABLE  = "available"
    ASSIGNED = "assigned"
    REPAIR = "repair"


class Asset(BaseModel):
    id : int
    asset_tag : Optional[str]  #unique QR string
    category : str
    model : Optional[str]
    serial_number : int
    ative_status : Status

