from datetime import datetime

from pydantic import BaseModel


class JWTMeta(BaseModel):
    exp: datetime
    subject: str


