from pydantic import BaseModel, UUID4
from typing import Optional

class UserBase(BaseModel):
    username: str
    password: str

class UserInDBBase(UserBase):
    id: int
    
    class Config:
        orm_mode = True

class UserInDB(UserInDBBase):
    password: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str
