from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id : int
    name : str
    emai : str
    department : str
