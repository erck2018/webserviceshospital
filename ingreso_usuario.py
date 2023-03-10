import requests
import json

url = "http://zafiroapi.sispropreprod.gov.co:8081/api/Login"

payload = json.dumps({
  "tipoIdentificacion": "CC",
  "Identificacion": "779713047",
  "Password": "Pruebas123"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
response_dict = response.json()

token = response_dict.get('token')
#print(response.text)
print(token)
print(response.text)

#variable="token"
#authen=f"beard {token}"