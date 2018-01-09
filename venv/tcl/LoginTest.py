# coding=utf-8

import requests
import json


headers = {'Content-Type': 'application/json'}
payload = {"userPassword":"12345678","deviceId":"ffffffff-e074-16ee-0000-00007a464159","language":"US","areaCode":"+86","deviceName":"SM-C7010","userPhone":"15121094359","pushId":"bf9b21d44db440419ecb47d9376f3eda"}
url = "https://srv888.anytime.exchange/server/login"
r = requests.post(url, data = json.dumps(payload), headers = headers, verify = False)

se2 = r.json()
sessionTokenValue=''

print  type(se2)
for i in se2:
    if i == 'sessionToken':
        sessionTokenValue=se2[i]

print sessionTokenValue







