#!/usr/bin/env bash

set -xe
# wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
./ngrok http 5000 -bind-tls=true -config config/ngrok.yaml -log=stdout &
sleep 10
python hello_bot.py &
bash
