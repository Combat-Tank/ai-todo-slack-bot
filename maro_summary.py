from pydantic import BaseModel
from langchain_google_vertexai import VertexAI


# Message model
# text: The plain text content of the message.
# ts: The unique timestamp for the message within the channel.
# user: The ID of the user who sent the message.
# attachments: A list of attachment objects (if any).

model = VertexAI(model_name="gemini-pro")


class Message(BaseModel):
    user_id: str
    ts: str
    text: str


knowledge_base = [
    Message(user_id="maro", ts="1712340030", text="Welcome the new team member Nils"),
    Message(user_id="maro", ts="1712340035", text="We have a new team member Max!!"),
    Message(user_id="maro", ts="1712340038", text="Welcome Ribeiro!!"),
]

context = ""
for message in knowledge_base:
    context += message.text + "\n"

message = f"Can you give me a summary of what happened today? I have these messages as context: {context}"
res = model.invoke(message)

print(res)
