from pydantic import BaseModel
from langchain_google_vertexai import VertexAI
import time


class SlackMessage(BaseModel):
    user_id: str
    ts: str
    text: str


def decideToDo(message: SlackMessage):
    model = VertexAI(model_name="gemini-pro")
    res = model.invoke(f'''"Using natural language processing, determine if the following message contains a task that can be interpreted as a to-do item:

```
{message.text}
```

Provide a binary response: yes or no."''')
    return res


def createToDoText(message: SlackMessage):
    model = VertexAI(model_name="gemini-pro")
    res = model.invoke(
        f'''Using natural language processing, determine what task the following message from {message.user_id} contains for me:

```
{message.text}
```

Provide only a to-do item as response:''')
    return res


def createToDoTime(message: SlackMessage):
    model = VertexAI(model_name="gemini-pro")
    res = model.invoke(f'''Using natural language processing, classify how urgent the task from the following message is for me:

```
{message}
```

The classes are "urgent", "neutral" and "not urgent".
Respond with the class name. By default reply with "neutral"''')
    return res


message = SlackMessage(text="Bring me flowers. Be fast.", user_id="Nils", ts=str(time.time()))

print(createToDoTime(message))
