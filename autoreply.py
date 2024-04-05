import decision_maker
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from langchain_google_vertexai import VertexAI
import os
import json

from maro_summary import save_message_for_summary, Message

app = Flask(__name__)

SLACK_TOKEN = os.getenv('TOKEN')

model = VertexAI(model_name="gemini-pro")
client = WebClient(token=SLACK_TOKEN)


@app.route("/slack/events", methods=["POST"])
def slack_events():
    # Slack sends a challenge request to verify the endpoint
    if "challenge" in request.json:
        return jsonify({
            "challenge": request.json["challenge"]
        })

    elif "event" in request.json:
        response = decision_maker.autoReply(request.json["event"]["text"], model)
        try:
            print(json.dumps(request.json))
            client.chat_postMessage(text=response, channel=request.json["event"]["channel"])
        except SlackApiError as e:
            print(f"Error fetching messages: {e}")

        save_message_for_summary(Message(
            user=request.json["event"]["user"],
            ts=request.json["event"]["ts"],
            text=request.json["event"]["text"],
            priority=1
        ))

    # Your code to handle incoming events goes here

    return "OK", 200


if __name__ == "__main__":
    app.run(port=3000)
