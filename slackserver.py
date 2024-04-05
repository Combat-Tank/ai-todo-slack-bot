from flask import Flask, request, jsonify, redirect
import requests
from urllib.parse import quote
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

app = Flask(__name__)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    # Slack sends a challenge request to verify the endpoint
    if "challenge" in request.json:
        return jsonify({
            "challenge": request.json["challenge"]
        })

    elif "event" in request.json:
        print(request.json)

    # Your code to handle incoming events goes here

    return "OK", 200

if __name__ == "__main__":
    app.run(port=3000)