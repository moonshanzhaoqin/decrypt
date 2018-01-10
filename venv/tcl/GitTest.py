import requests

cs_url  = 'https://api.github.com'
cs_user = 'shanzhaoqin@gmail.com'
cs_psw  = 'Sq123456'

r = requests.get(cs_url, auth=(cs_user, cs_psw), verify = False)
print r.status_code
print

if requests.codes.ok == r.status_code:
    for k, v in r.json().items():
        print k, v