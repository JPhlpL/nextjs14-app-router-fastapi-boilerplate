from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    email: str
    username: str
    password: str
    firstName: Optional[str]
    lastName: Optional[str]

    class Config:
        from_attributes = True
