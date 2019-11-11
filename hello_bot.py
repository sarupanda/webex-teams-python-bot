#!/usr/bin/env python

import json

from flask import Flask, request
from webexteamssdk import WebexTeamsAPI, Webhook
import requests

flask_app = Flask(__name__)
teams_api = None

def get_ngrok_url(addr='127.0.0.1', port=4040):
    """Queries ngrok JSON API and returns public URL if ngrok is running"""
    try:
        ngrokpage = requests.get("http://{}:{}/api/tunnels".format(addr, port), headers="").text
    except:
        raise RuntimeError('Not able to connect to ngrok API')
    ngrok_info = json.loads(ngrokpage)
    url = ngrok_info['tunnels'][0]['public_url']
    return url

@flask_app.route('/teamswebhook', methods=['POST'])
def teamswebhook():
    """/teamswebhook endpoint, takes POST requests"""

    if request.method == 'POST':
        json_data = request.json
        webhook_obj = Webhook(json_data)

        # Obtain room, message, person and email info using the Teams API
        room = teams_api.rooms.get(webhook_obj.data.roomId)
        message = teams_api.messages.get(webhook_obj.data.id)
        person = teams_api.people.get(message.personId)
        email = person.emails[0]

        # Message was sent by the bot, do not respond.
        me = teams_api.people.me()
        if message.personId == me.id:
            return 'Ignore'
        else:
            teams_api.messages.create(room.id, text='Hello, person who has email '+str(email))
            return 'OK'


if __name__ == '__main__':
    teams_api = WebexTeamsAPI(access_token='')

    # Automatically grab ngrok URL
    ngrok_url = get_ngrok_url()

    # Delete existing webhook if it exists
    webhook_name = 'hello-bot-webhook'
    dev_webhook = None
    webhooks = teams_api.webhooks.list()
    for hook in webhooks:
        if hook.name == webhook_name:
            dev_webhook = hook
    if dev_webhook:
        teams_api.webhooks.delete(dev_webhook.id)

    # Create new webhook
    teams_api.webhooks.create(
        name=webhook_name, targetUrl=ngrok_url + '/teamswebhook', resource='messages',
        event='created', filter=None
    )

    # Host flask server on port 5000
    flask_app.run(host='0.0.0.0', port=5000)
