import requests
import json

url = "https://dnaspaces.io/api/location/v1/clients"
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYnkiOiJMb2NhdGlvbiIsInR5cGUiOiJCZWFyZXIiLCJ0ZW5hbnRJZCI6MjExLCJ1c2VybmFtZSI6ImZsY29ycmVhQGNpc2NvLmNvbSIsImtleUlkIjoiOGMxNWZmMjMtNzY5My00YmYxLWE4NDktMzAxY2I3ODZkNGNjIiwidXNlcklkIjo2NywiaWF0IjoxNTgzMzMxNzkyLCJleHAiOjE1OTExMDc3OTJ9.1nP-PH8CnPMXO3I8kHDd23JClWiTvo1EUI-hseJ3Iss"
headers = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

response = requests.request("GET", url, headers=headers)
#json_date = (response.text)
#dna_date = (json.loads(json_date))
#print(response)
#tenants = (dna_date['results'])
myMacAddresses1 = ('00:0c:cc:55:04:e9')
myMacAddresses2 = ('00:18:60:8a:f0:c0')
myMacAddresses3 = ('00:04:f1:06:d5:33')
myMacAddresses4 = ('08:21:ef:d0:db:36')
myMacAddresses5 = ('bc:3b:af:9c:9c:e1')
#for tenant in tenants:
 #   if tenant["macAddress"] in myMacAddresses:
  #      print(json.dumps(tenant['coordinates'], indent=4, sort_keys=True))

dna_data = response.json()["results"]
#print(json.dumps(dna_data, indent=4))
for tenant in dna_data:
    if tenant["macAddress"] in myMacAddresses1:
        localidade_ventilador = (json.dumps(tenant["hierarchy"], indent=4, sort_keys=True))
      #  print(localidade_maca)
    
    if tenant["macAddress"] in myMacAddresses2:
        localidade_sonim = (json.dumps(tenant["hierarchy"], indent=4, sort_keys=True))
      #  print(localidade_cadeira)


    if tenant["macAddress"] in myMacAddresses3:
        localidade_cadeira = (json.dumps(tenant["hierarchy"], indent=4, sort_keys=True))
     #   print(localidade_cadeira3)

    if tenant["macAddress"] in myMacAddresses4:
        localidade_samsung = (json.dumps(tenant["hierarchy"], indent=4, sort_keys=True))
      #  print(localidade_cadeira4)

    if tenant["macAddress"] in myMacAddresses5:
        localidade_apple = (json.dumps(tenant["hierarchy"], indent=4, sort_keys=True))
     #   print(localidade_cadeira5)

