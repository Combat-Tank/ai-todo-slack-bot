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

### Try the slack integration

1. Go to: https://api.slack.com/apps/A06T2BX7HTM/oauth
2. Copy the xoxp token
3. Put it into a local bash var `export TOKEN="..."`
