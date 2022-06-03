import json
from common.poll import Poll
from flask import Flask, request
from common.utils import create_webhook
from webexteamssdk import WebexTeamsAPI, Webhook
from decouple import config

#WEBEX_TEAMS_ACCESS_TOKEN = '<bot-access-token>'
WEBEX_TEAMS_ACCESS_TOKEN = config('WEBEX_TEAMS_ACCESS_TOKEN')

teams_api = None
all_polls = {}

app = Flask(__name__)
@app.route('/messages_webhook', methods=['POST'])
def messages_webhook():
    if request.method == 'POST':
        webhook_obj = Webhook(request.json)
        return process_message(webhook_obj.data)

def process_message(data):
    if data.personId == teams_api.people.me().id:
        # Message sent by bot, do not respond
        return '200'
    else:
        message = teams_api.messages.get(data.id).text
        print(message)
        commands_split = (message.split())[1:]
        command = ' '.join(commands_split)
        parse_message(command, data.personEmail, data.roomId)
        return '200'

def parse_message(command, sender, roomId):
    if command == "create poll":
        if roomId not in list(all_polls.keys()):
            create_poll(roomId, sender)
    elif command == "add option":
        if all_polls[roomId]:
            add_option(roomId, sender)
    elif command == "start poll":
        if all_polls[roomId]:
            start_poll(roomId, sender)
    elif command == "end poll":
        if all_polls[roomId]:
            end_poll(roomId, sender)
    return

def generate_start_poll_card(roomId):
    return {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.1",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "Please type your poll name below"
                },
                {
                    "type": "Input.Text",
                    "id": "poll_name",
                    "placeholder": "Poll Name",
                    "maxLength": 100
                },
                {
                    "type": "TextBlock",
                    "text": "Please type your poll description below"
                },
                {
                    "type": "Input.Text",
                    "id": "poll_description",
                    "placeholder": "Poll Description",
                    "maxLength": 500,
                    "isMultiline": True
                },
                {
                    "type": "Input.Text",
                    "id": "roomId",
                    "value": roomId,
                    "isVisible": False
                }
            ],
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "OK"
                }
            ]
        }
    }

def generate_add_option_card(roomId):
    return {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.1",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "Please type the option you would like to add below:"
                },
                {
                    "type": "Input.Text",
                    "id": "option_text",
                    "placeholder": "Option Text",
                    "maxLength": 100
                },
                {
                    "type": "Input.Text",
                    "id": "roomId",
                    "value": roomId,
                    "isVisible": False
                }
            ],
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "OK"
                }
            ]
        }
    }

def generate_voting_card(roomId):
    poll = all_polls[roomId]
    voting_options = {
        "type": "Input.ChoiceSet",
        "id": "poll_choice",
        "style": "expanded",
        "value": "1",
        "choices": []
    }
    for value, option in poll.options.items():
        voting_options["choices"].append({"title": option, "value": str(value)})
    return {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.1",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "Have your say on the poll below!",
                    "size": "large"
                },
                {
                    "type": "TextBlock",
                    "text": all_polls[roomId].name,
                    "size": "medium"
                },
                {
                    "type": "TextBlock",
                    "text": all_polls[roomId].description,
                    "weight": "bolder"
                },
                {
                    "type": "Input.Text",
                    "id": "roomId",
                    "value": roomId,
                    "isVisible": False
                },
                voting_options
            ],
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "OK"
                }
            ]
        }
    }

def generate_results_card(roomId, results):
    card_results = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.1",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "Below are the results!",
                    "size": "large"
                },
                {
                    "type": "Input.Text",
                    "id": "roomId",
                    "value": roomId,
                    "isVisible": False
                }
            ],
            "actions": []
        }
    }
    for option, total in results.items():
        card_results["content"]["body"].append({
            "type": "TextBlock",
            "text": option + ": *" + str(total) + "*"
        })
    return card_results

def create_poll(roomId, sender):
    teams_api.messages.create(toPersonEmail=sender, text="Cards Unsupported", attachments=[generate_start_poll_card(roomId)])

def add_option(roomId, sender):
    teams_api.messages.create(toPersonEmail=sender, text="Cards Unsupported", attachments=[generate_add_option_card(roomId)])

def start_poll(roomId, sender):
    if all_polls[roomId].author == sender:
        if not all_polls[roomId].started:
            all_polls[roomId].started = True
            teams_api.messages.create(roomId=roomId, text="Cards Unsupported", attachments=[generate_voting_card(roomId)])
        else:
            send_message_in_room(roomId, "Error: poll already started")
    else:
        send_message_in_room(roomId, "Error: only the poll author can start the poll")

def end_poll(roomId, sender):
    if all_polls[roomId].author == sender:
        if all_polls[roomId].started:
            all_polls[roomId].started = False
            teams_api.messages.create(roomId=roomId, text="Card Unsupported", attachments=[generate_results_card(roomId, all_polls[roomId].collate_results())])
        else:
            send_message_in_room(roomId, "Error: poll hasn't been started yet")
    else:
        send_message_in_room(roomId, "Error: only the poll's author can end the poll")

@app.route('/attachmentActions_webhook', methods=['POST'])
def attachmentActions_webhook():
    if request.method == 'POST':
        print("attachmentActions POST!")
        webhook_obj = Webhook(request.json)
        return process_card_response(webhook_obj.data)

def process_card_response(data):
    attachment = (teams_api.attachment_actions.get(data.id)).json_data
    inputs = attachment['inputs']
    if 'poll_name' in list(inputs.keys()):
        add_poll(inputs['poll_name'], inputs['poll_description'], inputs['roomId'], teams_api.people.get(data.personId).emails[0])
        send_message_in_room(inputs['roomId'], "Poll created with title: " + inputs['poll_name'])
    elif 'option_text' in list(inputs.keys()):
        current_poll = all_polls[inputs['roomId']]
        current_poll.add_option(inputs['option_text'])
        send_message_in_room(inputs['roomId'], "Option added to poll \"" + current_poll.name + "\": " + inputs['option_text'])
        print(current_poll.name)
        print(current_poll.options)
    elif 'poll_choice' in list(inputs.keys()):
        current_poll = all_polls[inputs['roomId']]
        current_poll.votes[int(inputs["poll_choice"])] += 1
    return '200'

def add_poll(poll_name, poll_description, room_id, author):
    print(author)
    poll = Poll(poll_name, poll_description, room_id, author)
    all_polls[room_id] = poll

def send_direct_message(person_email, message):
    teams_api.messages.create(toPersonEmail=person_email, text=message)

def send_message_in_room(room_id, message):
    teams_api.messages.create(roomId=room_id, text=message)

if __name__ == '__main__':
    teams_api = WebexTeamsAPI(access_token=WEBEX_TEAMS_ACCESS_TOKEN)
    create_webhook(teams_api, 'messages_webhook', '/messages_webhook', 'messages')
    create_webhook(teams_api, 'attachmentActions_webhook', '/attachmentActions_webhook', 'attachmentActions')
    app.run(host='0.0.0.0', port=12000)