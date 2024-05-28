from pydantic import BaseModel, UUID4
from typing import Optional

class TokenData(BaseModel):
    username: Optional[str] = None