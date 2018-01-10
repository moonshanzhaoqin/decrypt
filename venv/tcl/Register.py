# coding=utf-8

import requests
import json

def getVerify():
    headers1 = {'Content-Type': 'application/json'}
    payload1 = {"userPhone": "65230068","areaCode": "+853","purpose": "REGISTER"}
    url1 = "https://srv888.anytime.exchange/server/getVerificationCode"
    r = requests.post(url1, data = json.dumps(payload1), headers = headers1, verify = False)
    print r.status_code


def register():
    headers = {'Content-Type': 'application/json'}
    payload = {
        "deviceId": "ffffffff-e074-16ee-0000-00007a464159",
        "areaCode": "+853",
        "registrationCode": "654321",
        "userPassword": "12345678",
        "language": "zh",
        "userName": "pythonOne",
        "deviceName": "SM-C7010",
        "userPhone": "65230068",
        "pushId": "5267c206f1694648a141688d9b2c6eb0"
    }
    url = "https://srv888.anytime.exchange/server/register"
    r = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    se2 = r.json()
    print se2

if __name__ == '__main__':
    getVerify()
    register()



















