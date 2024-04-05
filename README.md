# ai-todo-slack-bot
Slack Bot using AI for creation of TO-DO lists

# Getting started

1. Create a virtual env `virtualenv venv`
2. Activate it `source venv/bin/activate` (you should have a prefix in your bash command line `(venv)`)
3. Install the stuff `pip install -r requirements.txt`
4. Run `python main.py`

## Set up Slack

1. Create the file `.env.local` from `.env.local.template`
2. Get the Client ID and Secret from: https://api.slack.com/apps/A06T1HW5UH1/general? and put those into the `.env.local`
3. When authenticating you are redirected back to a URL. You need to expose your local URL. VSCode has ports for that. (Clarify how to do that without VSCode)
4. Start `slackserver.py`

### Get a token

1. You need to have a public accessible URL (I believe)
   - You can do that in VSCode by going to PORTS and adding a port (for now make it public)
2. Add your base URL to https://api.slack.com/apps/A06T1HW5UH1/oauth
3. Go to <http://localhost:3000>
4. Check the output in the terminal for the access token

### Send a message

You can use the `/slack/message` endpoint e.g. via curl if you store the token in the bash var `TOKEN`

```sh
curl -X POST http://localhost:3000/slack/message \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"channel":"C06SYHHSDEH", "message":"Dude Slackoff! :wink:"}'
```
