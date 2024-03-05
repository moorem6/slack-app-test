import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initialize app with bot token and socket mode handler
with open("SLACK_BOT_TOKEN", "r") as f:
    SLACK_BOT_TOKEN = f.read().strip()

with open("SLACK_APP_TOKEN", "r") as f:
    SLACK_APP_TOKEN = f.read().strip()

app = App(token=SLACK_BOT_TOKEN)

'''
# basic call and response to any message that has hello in it
@app.message("hello")
def message_hello(message, say):
    print('received a hello')
    say(f"Hey there <@{message['user']}>!")
    # say(f"Hey there!")
'''

@app.message("hello")
def message_hello(message, say):
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there again <@{message['user']}>!"
    )

@app.action("button_click")
def action_button_click(body, ack, say):
    ack()
    say(f"<@{body['user']['id']}> clicked the button")


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
