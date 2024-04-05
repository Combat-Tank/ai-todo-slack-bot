from langchain_google_vertexai import VertexAI

from Message import Message
from sqlloader import get_all_messages_for_user, save_message_for_user

# Message model
# text: The plain text content of the message.
# ts: The unique timestamp for the message within the channel.
# user: The ID of the user who sent the message.
# attachments: A list of attachment objects (if any).

model = VertexAI(model_name="gemini-pro")

def create_summary():
    messages = get_all_messages_for_user('receiver name')
    context = ""
    for message in messages:
        context += message.text + "\n"
        if len(context) > 5000:
            break

    prompt = f"Can you give me a summary of what happened today? I have these messages as context: {context}"
    res = model.invoke(prompt)

    return res



# knowledge_base = [
#     Message(user_id="maro", ts="1712340030", text="Welcome the new team member Nils"),
#     Message(user_id="maro", ts="1712340035", text="We have a new team member Max!!"),
#     Message(user_id="maro", ts="1712340038", text="Welcome Ribeiro!!"),
# ]

# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
# import os
#
# SLACK_TOKEN = os.getenv("TOKEN")
#
# client = WebClient(token=SLACK_TOKEN)
#
# Message
#
# channel_id = "C06SYHHSDEH"
#
# messages = []
# try:
#     # Fetch recent messages from a channel
#     response = client.conversations_history(channel=channel_id)
#     messages = response.data["messages"]
# except SlackApiError as e:
#     print(f"Error fetching messages: {e}")
#
if __name__=="__main__":
    print(create_summary())

def save_message_for_summary(message: Message):
    save_message_for_user(message, "receiver name")
    print('success')
