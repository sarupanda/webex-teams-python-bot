#!/usr/bin/env python

import json
import requests
from flask import Flask, request
from webexteamssdk import WebexTeamsAPI, Webhook

WEBEX_TEAMS_ACCESS_TOKEN = '<my-bot-access-token>'
teams_api = None

app = Flask(__name__)
@app.route('/teamswebhook', methods=['POST'])
def teamswebhook():
    if request.method == 'POST':
        webhook_obj = Webhook(request.json)
        return process_message(webhook_obj.data)

def create_webhook(name):
    delete_webhook(name)
    teams_api.webhooks.create(
        name=name, targetUrl=get_ngrok_url()+'/teamswebhook',
        resource='messages', event='created', filter=None)

def delete_webhook(name):
    for hook in teams_api.webhooks.list():
        if hook.name == name:
            teams_api.webhooks.delete(hook.id)

def get_ngrok_url(addr='127.0.0.1', port=4040):
    try:
        ngrokpage = requests.get("http://{}:{}/api/tunnels".format(addr, port), headers="").text
    except:
        raise RuntimeError('Not able to connect to ngrok API')
    ngrok_info = json.loads(ngrokpage)
    return ngrok_info['tunnels'][0]['public_url']

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
    create_webhook('bot-webhook')
    app.run(host='0.0.0.0', port=5000)
