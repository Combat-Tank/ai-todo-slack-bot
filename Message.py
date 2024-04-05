from pydantic import BaseModel
class Message(BaseModel):
    user: str
    ts: str
    text: str
    priority: int