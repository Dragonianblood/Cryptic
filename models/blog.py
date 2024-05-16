from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel
from beanie import Document, Indexed


class Blogs(Document):
    title: Indexed(str, unique=True)
    description: str
    body: Optional[str] = None
    author: str
    timeStamp: datetime
    imageLink: Optional[str] = None


    class Settings:
        name = "blogs"
