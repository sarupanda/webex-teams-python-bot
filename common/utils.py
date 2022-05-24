import json
import requests

def create_webhook(teams_api, name, webhook, resource):
    delete_webhook(teams_api, name)
    teams_api.webhooks.create(
        name=name, targetUrl=get_ngrok_url()+webhook,
        resource=resource, event='created', filter=None)

def delete_webhook(teams_api, name):
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