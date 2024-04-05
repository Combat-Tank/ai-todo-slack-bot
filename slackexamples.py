from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

SLACK_TOKEN = os.getenv('TOKEN')

client = WebClient(token=SLACK_TOKEN)

channel_id = "C06SYHHSDEH"

try:
    # Fetch recent messages from a channel
    response = client.chat_postMessage(channel=channel_id, text="Hey everyone!")

    # Process messages (this is a simplified example)
    print("Message sent")
except SlackApiError as e:
    print(f"Error fetching messages: {e}")

try:
    # Fetch recent messages from a channel
    response = client.conversations_history(channel=channel_id)
    messages = response.data['messages']

    # Process messages (this is a simplified example)
    for message in messages:
        print(message)
except SlackApiError as e:
    print(f"Error fetching messages: {e}")


try:
    response = client.reminders_add(
        text="Reminder text",
        time="in 10 minutes"  # Or a specific time/date
    )
    print("Reminder created:", response['reminder']['id'])
except SlackApiError as e:
    print(f"Error creating reminder: {e}")