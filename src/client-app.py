from random import randint
import requests

# Lista de endopints
endpoints = ['renda-fixa', 'renda-variavel', 'acoes', 'fiis', 'criptos']

# URL da API
url = 'http://app:5000/'

while True:
    # Faz a solicitação e recebe a resposta
    resposta = requests.get(url + endpoints[randint(0, 3)])
    print(resposta.status_code)
