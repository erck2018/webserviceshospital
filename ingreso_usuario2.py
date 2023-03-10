import requests
import json

url2 = "http://zafiroapi.sispropreprod.gov.co:8081/api/Login"
url = "https://paiwebws.paiweb.gov.co:8082/api/interop/RegSolicitudCambioEstrategia"
payload1 = json.dumps({
  "tipoIdentificacion": "CC",
  "Identificacion": "779713047",
  "Password": "Pruebas123"
})
headers1 = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url2, headers=headers1, data=payload1)
response_dict = response.json()

token = response_dict.get('token')

print(token)

payload2 = json.dumps({
  "TipoDocumento": "CC",
  "NroDocumento": "1116243960",
  "PrimerNombre": "JUAN",
  "PrimerApellido": "QUINTERO",
  "FechaNacimiento": "1989-02-03",
  "Sexo": "M",
  "CodigoInstitucion": "768340170801",
  "CodigoVacuna": 20217,
  "NroDosis": 0,
  "TipoEsquema": 3,
  "CodigoEstrategia": 4,
  "FechaAplicacion": "2021-07-23",
  "CorreoElectronico": "vacunacioncovid@hospitalrubencruzvelez.gov.co"
})
headers2 = {
  'Authorization': f'Bearer {token}',
  'Content-Type': 'application/json'
}

response2 = requests.request("POST", url, headers=headers2, data=payload2)
response_dict2 = response2.json()
cambio_codigo = response_dict2.get('idSolicitudCambio')
print(response2.text)
print(cambio_codigo)
url3 = f"https://paiwebws.paiweb.gov.co:8082/api/interop/ConsSolicitudCambioEstrategia/{cambio_codigo}"

payload3={}
headers3 = {
 'Authorization': f'Bearer {token}'
}

response3 = requests.request("GET", url3, headers=headers3, data=payload3)

print(response3.text)