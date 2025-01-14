from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

class User(BaseModel):
    #id: UUID
    email: str
    username: str
    password: str
    firstName: Optional[str]
    lastName: Optional[str]

    class Config:
        from_attributes = True
