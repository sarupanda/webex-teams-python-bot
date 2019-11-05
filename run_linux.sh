#!/usr/bin/env bash

set -xe
./ngrok http 5000 -bind-tls=true -config config/ngrok.yaml -log=stdout &
sleep 10
python hello_bot.py &
bash
