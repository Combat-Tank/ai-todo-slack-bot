import decision_maker
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from langchain_google_vertexai import VertexAI
import os
import json
from Message import Message
from ToDo import decideToDo, createToDoText, createToDoTime
from maro_summary import save_message_for_summary

app = Flask(__name__)

SLACK_TOKEN = os.getenv("TOKEN")

model = VertexAI(model_name="gemini-pro")
client = WebClient(token=SLACK_TOKEN)
# identity = client.users_identity()
# userid = identity["user"]["id"]


@app.route("/slack/events", methods=["POST"])
def slack_events():
    # Slack sends a challenge request to verify the endpoint
    if "challenge" in request.json:
        return jsonify({"challenge": request.json["challenge"]})

    elif "event" in request.json:
        # if request.json["event"]["user"] == userid:
        #     print("ignoring your own message")
        #     return
        response = decision_maker.autoReply(request.json["event"]["text"], model)
        reaction = decision_maker.autoReact(request.json["event"]["text"], model)
        try:
            if response["replyBool"]:
                client.chat_postMessage(
                    text=response["reply"], channel=request.json["event"]["channel"]
                )
            else:
                print("No reply")

            if response["emojiReply"]:
                client.reactions_add(
                    name=reaction["emoji"],
                    timestamp=request.json["event"]["ts"],
                )
            else:
                print("No emoji")
        except SlackApiError as e:
            print(f"Error fetching messages: {e}")

        message = Message(
            user=request.json["event"]["user"],
            ts=request.json["event"]["ts"],
            text=request.json["event"]["text"],
            priority=1,
        )
        save_message_for_summary(message)
        if decideToDo(message) == "yes":
            todoText = createToDoText(message)
            todoTime = createToDoTime(message)
            try:
                response = client.reminders_add(text=todoText, time=todoTime)
                print("Reminder created:", response["reminder"]["id"])
            except SlackApiError as e:
                print(f"Error creating reminder: {e}")

    # Your code to handle incoming events goes here

    return "OK", 200


if __name__ == "__main__":
    app.run(port=3000)
