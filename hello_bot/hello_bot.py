#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import os

# 3rd party imports ------------------------------------------------------------
# Flask help can be found here:
# http://flask.pocoo.org/
from flask import Flask, request
from webexteamssdk import WebexTeamsAPI, Webhook

# local imports ----------------------------------------------------------------
from utilities import get_ngrok_url, find_webhook_by_name, delete_webhook, create_webhook

flask_app = Flask(__name__)
teams_api = None

# Use a python decorator which tells Flask to execute this method when the "/teamswebhook" endpoint
# is hit and the HTTP method is a "POST" request. 
@flask_app.route('/teamswebhook', methods=['POST'])
def teamswebhook():

    # Only execute this section of code when a POST request is sent, as a POST indicates when a
    # message has been sent and therefore needs processing.
    if request.method == 'POST':
        json_data = request.json
        print(f"\nWEBHOOK POST RECEIVED: {json_data}\n")

        # Pass the JSON data so that it can get parsed by the Webhook class
        webhook_obj = Webhook(json_data)

        # Obtain information about the request data such as room, message, the person it came from 
        # and person's email address. 
        room = teams_api.rooms.get(webhook_obj.data.roomId)
        message = teams_api.messages.get(webhook_obj.data.id)
        person = teams_api.people.get(message.personId)
        email = person.emails[0]

        print("NEW MESSAGE IN ROOM '{}'".format(room.title))
        print("FROM '{}'".format(person.displayName))
        print("MESSAGE '{}'\n".format(message.text))

        # Message was sent by the bot, do not respond.
        # At the moment there is no way to filter this out, there will be in the future
        me = teams_api.people.me()
        if message.personId == me.id:
            return 'OK'
        else:
            teams_api.messages.create(room.id, text='Hello, person who has email '+str(email))
    else:
        print('received none post request, not handled!')


if __name__ == '__main__':
    teams_api = WebexTeamsAPI(access_token='')

    # Get some required NGrok information
    ngrok_url = get_ngrok_url()

    # Define the name of webhook
    webhook_name = 'hello-bot-wb-hook'

    # Find any existing webhooks with this name and if this already exists then delete it
    dev_webhook = find_webhook_by_name(teams_api, webhook_name)
    if dev_webhook:
        delete_webhook(teams_api, dev_webhook)

    # Create a new teams webhook with the name defined above 
    create_webhook(teams_api, webhook_name, ngrok_url + '/teamswebhook')

    # Host flask web server on port 5000
    flask_app.run(host='0.0.0.0', port=5000)
