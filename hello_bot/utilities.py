import json
import re
from pprint import pprint
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

# ngrok utilities
def get_ngrok_url(addr='127.0.0.1', port=4040):
    ngrokjson = ''
    try:
        ngrokpage = requests.get("http://{}:{}/api/tunnels".format(addr, port), headers="").text
    except:
        raise RuntimeError('Not able to connect to ngrok webui')
    ngrok_info = json.loads(ngrokpage)
    pprint(ngrok_info)
    url = ngrok_info['tunnels'][0]['public_url']
    return url

# webhook utilities
def delete_webhook(api, webhook):
    api.webhooks.delete(webhook.id)


def find_webhook_by_name(api, name):
    webhooks = api.webhooks.list()
    for hook in webhooks:
        if hook.name == name:
            return hook
    return False


def create_webhook(api, name, target_url,
                   resource='messages',
                   event='created',
                   filter=None):
    res = api.webhooks.create(name=name,
                              targetUrl=target_url,
                              resource=resource,
                              event=event,
                              filter=filter)
    return res

