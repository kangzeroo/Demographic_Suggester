import requests
import json

def sendOffToNode(leaseObj):
    jsonLease = json.dumps(leaseObj)
    headers = {'content-type': 'application/json'}
    print(jsonLease)
    r = requests.post('http://localhost:7201/new_kijiji_property', data=jsonLease, headers=headers)
    print(r)
