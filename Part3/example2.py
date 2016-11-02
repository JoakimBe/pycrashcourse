import requests
import json

ip = "10.128.1.200"
port = "443"
username = "admin"
password = "temp123"


def api_call(ip, port, command, json_payload, sid):
    url = "https://{ip}:{port}/web_api/{command}".format(ip=ip, port=port, command=command)

    if len(sid) <= 0:
        request_headers = {'Content-Type': 'application/json'}
    else:
        request_headers = {'Content-Type': 'application/json', 'X-chkp-sid': sid}

    r = requests.post(url, data=json.dumps(json_payload), headers=request_headers, verify=False)
    return r.json()

