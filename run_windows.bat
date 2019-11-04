@echo off
START /b cmd /c ngrok.exe http 5000 -bind-tls=true -config config\ngrok.yaml -log=stdout
SLEEP 10
python hello_bot\hello_bot.py