import requests

url = "http://api.airvisual.com/v2/nearest_city?key=94526d74-8c70-4eba-99a5-9fc494d14f58"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
