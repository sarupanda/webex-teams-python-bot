#!/usr/bin/env python

import json
from flask import Flask, request
from webexteamssdk import WebexTeamsAPI, Webhook
from utils import create_webhook

WEBEX_TEAMS_ACCESS_TOKEN = '<my-bot-access-token>'
teams_api = None

app = Flask(__name__)
@app.route('/teamswebhook', methods=['POST'])
def teamswebhook():
    if request.method == 'POST':
        webhook_obj = Webhook(request.json)
        return process_message(webhook_obj.data)

def process_message(data):
    sender = teams_api.people.get(data.personId)
    message = 'Hi ' + sender.displayName
    message += ', your message was \"' + teams_api.messages.get(data.id).text + '\"'

    if data.personId == teams_api.people.me().id:
        # Message sent by bot, do not respond
        return ''
    else:
        if data.roomType == 'direct':
            send_direct_message(data.personEmail, message)
        if data.roomType == 'group':
            send_message_in_room(data.roomId, message)
        return '200'

def send_direct_message(person_email, message):
    teams_api.messages.create(toPersonEmail=person_email, text=message)

def send_message_in_room(room_id, message):
    teams_api.messages.create(roomId=room_id, text=message)

if __name__ == '__main__':
    teams_api = WebexTeamsAPI(access_token=WEBEX_TEAMS_ACCESS_TOKEN)
    create_webhook(teams_api, 'bot-webhook')
    app.run(host='0.0.0.0', port=5000)
