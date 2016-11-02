import requests
import json

ip = "10.128.1.200"
port = "443"
username = "admin"
password = "temp123"
command = "publish"
sid = "vI-qc6oZQM5uHrFoqHoHWZLFIUBk3YPsshhT5k-wKZ0"

json_payload = {

}


url = "https://{ip}:{port}/web_api/{command}".format(ip=ip, port=port, command=command)

#request_headers = {'Content-Type': 'application/json'}
request_headers = {'Content-Type': 'application/json', 'X-chkp-sid': sid}

r = requests.post(url, data=json.dumps(json_payload), headers=request_headers, verify=False)
print(json.dumps(r.json(), sort_keys=False, indent=4, separators=(',', ':')))
