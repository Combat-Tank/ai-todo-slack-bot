from pydantic import BaseModel
from langchain_google_vertexai import VertexAI
import time

from Message import Message


def decideToDo(message: Message):
    model = VertexAI(model_name="gemini-pro")
    res = model.invoke(
        f'''"Using natural language processing, determine if the following message contains a task that can be interpreted as a to-do item:

```
{message.text}
```

Provide a binary response: yes or no."'''
    )
    return res


def createToDoText(message: Message):
    model = VertexAI(model_name="gemini-pro")
    res = model.invoke(
        f"""Using natural language processing, determine what task the following message from {message.user} contains for me:

```
{message.text}
```

Provide only a to-do item as response:"""
    )
    return res


def createToDoTime(message: Message):
    model = VertexAI(model_name="gemini-pro")
    res = model.invoke(
        f'''Using natural language processing, classify how urgent the task from the following message is for me:

```
{message}
```

The classes are "urgent", "neutral" and "not urgent".
Respond with the class name. By default reply with "neutral"'''
    )
    if res == "urgent":
        return "in 1 hour"
    elif res == "neutral":
        return "in 1 day"
    elif res == "not urgent":
        return "in 1 week"
