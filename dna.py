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

imagem = cv2.imread("sonic.jpg", 1)
#for tenant in tenants:
 #   if tenant["macAddress"] in myMacAddresses:
  #      print(json.dumps(tenant['coordinates'], indent=4, sort_keys=True))

dna_data = response.json()["results"]
#print(json.dumps(dna_data, indent=4))


for tenant in dna_data:
    if tenant["macAddress"] in myMacAddresses1:
        localidade_ventilador = (json.dumps(tenant["hierarchy"], indent=4, sort_keys=True))
        #print(localidade_ventilador)
        if tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Corridor":
            localidade_ventilador = ('Corredor')
          #  print (localidade_ventilador)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Retail":
            localidade_ventilador = ('Retail')
           # print (localidade_ventilador)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>e-Cafe":
            localidade_ventilador = ('e-Cafe')
           # print (localidade_ventilador)
            
        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Education":
            localidade_ventilador = ('Educação')
           # print (localidade_ventilador)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Lobby":
            localidade_ventilador = ('Lobby')
           # print (localidade_ventilador)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Smartgrid":
            localidade_ventilador = ('Smartgrid')
           # print (localidade_ventilador)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Reception":
            localidade_ventilador = ('Recepção')
           # print (localidade_ventilador)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>PSS":
            localidade_ventilador = ('PSS')
            print (localidade_ventilador)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor":
            localidade_ventilador = ('Infelizmente não identificamos em qual área do 12ºAndar se encontra o cliente')
           # print (localidade_ventilador)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Healthcare":
            localidade_ventilador = ('Healthcare')
           # print (localidade_ventilador)


#localidade_sonim
    
    if tenant["macAddress"] in myMacAddresses2:
        localidade_sonim = (json.dumps(tenant["hierarchy"], indent=4, sort_keys=True))
     #   print(localidade_sonim)
        if tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Corridor":
            localidade_sonim = ('Corredor')
          #  print (localidade_sonim)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Retail":
            localidade_sonim = ('Retail')
         #   print (localidade_sonim)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>e-Cafe":
            localidade_sonim = ('e-Cafe')
         #   print (localidade_sonim)
            
        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Education":
            localidade_sonim = ('Educação')
            print (localidade_sonim)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Lobby":
            localidade_sonim = ('Lobby')
        #    print (localidade_sonim)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Smartgrid":
            localidade_sonim = ('Smartgrid')
         #   print (localidade_sonim)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Reception":
            localidade_sonim = ('Recepção')
        #    print (localidade_sonim)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>PSS":
            localidade_sonim = ('PSS')
         #   print (localidade_sonim)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor":
            localidade_sonim = ('Infelizmente não identificamos em qual área do 12ºAndar se encontra o cliente')
       #     print (localidade_sonim)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Healthcare":
            localidade_sonim = ('Healthcare')
       #     print (localidade_sonim)
            
        
#localidadde_cadeira

    if tenant["macAddress"] in myMacAddresses3:
        localidade_cadeira = (json.dumps(tenant["hierarchy"], indent=4, sort_keys=True))
   #     print(localidade_cadeira)
        if tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Corridor":
            localidade_cadeira = ('Corredor')
     #       print (localidade_cadeira)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Retail":
            localidade_cadeira = ('Retail')
       #     print (localidade_cadeira)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>e-Cafe":
            localidade_cadeira = ('e-Cafe')
      #      print (localidade_cadeira)
            
        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Education":
            localidade_cadeira = ('Educação')
      #      print (localidade_cadeira)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Lobby":
            localidade_cadeira = ('Lobby')
      #      print (localidade_cadeira)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Smartgrid":
            localidade_cadeira = ('Smartgrid')
       #     print (localidade_cadeira)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Reception":
            localidade_cadeira = ('Recepção')
     #       print (localidade_cadeira)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>PSS":
            localidade_cadeira = ('PSS')
       #     print (localidade_cadeira)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor":
            localidade_cadeira = ('Infelizmente não identificamos em qual área do 12ºAndar se encontra o cliente')
      #      print (localidade_cadeira)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Healthcare":
            localidade_cadeira = ('Healthcare')
       #     print (localidade_cadeira)


#localidade_samsung

    if tenant["macAddress"] in myMacAddresses4:
        localidade_samsung = (json.dumps(tenant["hierarchy"], indent=4, sort_keys=True))
  #      print(localidade_samsung)
        if tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Corridor":
            localidade_samsung = ('Corredor')
     #       print (localidade_samsung)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Retail":
            localidade_samsung = ('Retail')
     #       print (localidade_samsung)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>e-Cafe":
            localidade_samsung = ('e-Cafe')
      ##      print (localidade_samsung)
            
        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Education":
            localidade_samsung = ('Educação')
    #        print (localidade_samsung)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Lobby":
            localidade_samsung = ('Lobby')
     #       print (localidade_samsung)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Smartgrid":
            localidade_samsung = ('Smartgrid')
     #       print (localidade_samsung)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Reception":
            localidade_samsung = ('Recepção')
   #         print (localidade_samsung)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>PSS":
            localidade_samsung = ('PSS')
    #        print (localidade_samsung)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor":
            localidade_samsung = ('Infelizmente não identificamos em qual área do 12ºAndar se encontra o cliente')
    #        print (localidade_samsung)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Healthcare":
            localidade_samsung = ('Healthcare')
    #        print (localidade_samsung)

#localidade apple

    if tenant["macAddress"] in myMacAddresses5:
   #     print (tenant['hierarchy'])
        if tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Corridor":
            localidade_apple = ('Corredor')
   #         print (localidade_apple)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Retail":
            localidade_apple = ('Retail')
    #        print (localidade_apple)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>e-Cafe":
            localidade_apple = ('e-Cafe')
   #         print (localidade_apple)
            
        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Education":
            localidade_apple = ('Educação')
   #         print (localidade_apple)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Lobby":
            localidade_apple = ('Lobby')
    #        print (localidade_apple)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Smartgrid":
            localidade_apple = ('Smartgrid')
    #        print (localidade_apple)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Reception":
            localidade_apple = ('Recepção')
   #         print (localidade_apple)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>PSS":
            localidade_apple = ('PSS')
   #         print (localidade_apple)
            
        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor":
            localidade_apple = ('Infelizmente não identificamos em qual área do 12ºAndar se encontra o cliente')
     #       print (localidade_apple)

        elif tenant["hierarchy"] == "ICRIO>RDJ3>12 floor>Healthcare":
            localidade_apple = ('Healthcare')
     #       print (localidade_apple)
