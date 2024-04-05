# ai-todo-slack-bot
Slack Bot using AI for creation of TO-DO lists

# Getting started

1. Create a virtual env `virtualenv venv`
2. Activate it `source venv/bin/activate` (you should have a prefix in your bash command line `(venv)`)
3. Install the stuff `pip install -r requirements.txt`
4. Run `python main.py`

### Try the slack integration

1. Go to: https://api.slack.com/apps/A06T2BX7HTM/oauth
2. Click *"Install to Workspace"*
2. Copy the xoxp token
3. Put it into a local bash var `export TOKEN="..."`
4. Set up the events here: https://api.slack.com/apps/A06T2BX7HTM/event-subscriptions?
   - You need to enable events for the user under *"Subscribe to events on behalf of users"*
      - `message.channels`
      - `message.groups`
      - `message.im`
      - `message.mpim`
5. Run it `python autoreply.py`
