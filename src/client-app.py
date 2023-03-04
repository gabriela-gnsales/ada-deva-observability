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
    # # Verifica o status da resposta
    # if resposta.status_code == 200:
    #     # Converte a resposta em JSON
    #     dados_renda_fixa = resposta.json()
    #     # Faz algo com os dados
    #     print(dados_renda_fixa)
    # else:
    #     # Caso haja algum erro
    #     print('Erro na requisição: {}'.format(resposta.status_code))

