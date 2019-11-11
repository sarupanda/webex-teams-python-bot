#!/usr/bin/env python

import json
import requests
from flask import Flask, request
from webexteamssdk import WebexTeamsAPI, Webhook

WEBEX_TEAMS_ACCESS_TOKEN = '<my-bot-access-token>'
flask_app = Flask(__name__)
teams_api = None

def create_webhook(name):
    delete_webhook(name)
    teams_api.webhooks.create(
        name=name, targetUrl=get_ngrok_url()+'/teamswebhook',
        resource='messages', event='created', filter=None)

def delete_webhook(name):
    for hook in teams_api.webhooks.list():
        if hook.name == webhook_name:
            teams_api.webhooks.delete(hook.id)

def get_ngrok_url(addr='127.0.0.1', port=4040):
    try:
        ngrokpage = requests.get("http://{}:{}/api/tunnels".format(addr, port), headers="").text
    except:
        raise RuntimeError('Not able to connect to ngrok API')
    ngrok_info = json.loads(ngrokpage)
    return ngrok_info['tunnels'][0]['public_url']

def process_message(data):
    person = teams_api.people.get(data.personId)
    room = teams_api.rooms.get(data.roomId)
    message = teams_api.messages.get(data.id)
    email = person.emails[0]

    me = teams_api.people.me()
    if message.personId == me.id:
        return ''
    else:
        teams_api.messages.create(room.id, text='Hello, person who has email '+str(email))
        return '200'

@flask_app.route('/teamswebhook', methods=['POST'])
def teamswebhook():
    if request.method == 'POST':
        webhook_obj = Webhook(request.json)
        return process_message(webhook_obj.data)

if __name__ == '__main__':
    teams_api = WebexTeamsAPI(access_token=WEBEX_TEAMS_ACCESS_TOKEN)
    webhook_name = 'bot-webhook'

    create_webhook(webhook_name)
    flask_app.run(host='0.0.0.0', port=5000)
