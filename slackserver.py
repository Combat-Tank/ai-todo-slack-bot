from flask import Flask, request, jsonify, redirect
from dotenv import load_dotenv
import requests
from urllib.parse import quote
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

app = Flask(__name__)

# Load environment variables from .env.local
load_dotenv(dotenv_path='.env.local')

# Access environment variables
SLACK_CLIENT_ID = os.getenv('SLACK_CLIENT_ID')
SLACK_CLIENT_SECRET = os.getenv('SLACK_CLIENT_SECRET')

redirect_uri = "https://l1j4rkm3-3000.euw.devtunnels.ms/slack/oauth_redirect"  # Make sure this matches the redirect URI in your app settings

@app.route("/login", methods=["GET"])
def login():
    scopes = "reminders:read,reminders:write"
    encoded_redirect_uri = quote(redirect_uri, safe='')

    auth_url = f"https://slack.com/oauth/v2/authorize?client_id={SLACK_CLIENT_ID}&scope={scopes}&redirect_uri={encoded_redirect_uri}"

    # Redirect the user to Slack's authorization page
    return redirect(auth_url)


@app.route("/slack/oauth_redirect", methods=["GET"])
def slack_oauth_redirect():
    code = request.args.get('code')
    if code:
        # Replace these with your app's Client ID and Client Secret
        client_id = SLACK_CLIENT_ID
        client_secret = SLACK_CLIENT_SECRET
        
        # Exchange the code for an access token
        response = requests.post("https://slack.com/api/oauth.v2.access", data={
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "redirect_uri": redirect_uri
        })

        data = response.json()
        if data.get("ok"):
            # Here, you might want to save the access token in a secure place
            access_token = data.get("authed_user").get("access_token")
            print(data)
            return "Authorization successful!"
        else:
            return "Error obtaining access token."
    else:
        return "No code provided by Slack.", 400

@app.route("/slack/message", methods=["POST"])
def send_message():
    token = request.headers.get('Authorization').split("Bearer ")[1]
    content = request.json
    channel = content.get('channel')
    message = content.get('message')

    client = WebClient(token=token)

    try:
        response = client.chat_postMessage(channel=channel, text=message)
        return jsonify({"ok": response["ok"], "message": "Message sent successfully"}), 200
    except SlackApiError as e:
        return jsonify({"ok": False, "error": str(e)}), 400

@app.route("/slack/events", methods=["POST"])
def slack_events():
    # Slack sends a challenge request to verify the endpoint
    if "challenge" in request.json:
        return jsonify({
            "challenge": request.json["challenge"]
        })

    # Your code to handle incoming events goes here

    return "OK", 200

if __name__ == "__main__":
    app.run(port=3000)