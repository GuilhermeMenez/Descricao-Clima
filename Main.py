import requests
from pprint import pprint

API_key = ''

cidade = input("Digite sua cidade\n")

base_url = 'http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid='+API_key

dados_clima = requests.get(base_url).json()

pprint(dados_clima)
