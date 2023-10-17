
import json
import requests
import pandas 

def buscar_dados():
    request = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    data = json.loads(request.content)
    valor_high = float(data["USDBRL"]["high"])
    return valor_high


def real_para_dolar( valorEmReal):
   valorAtualDolar = buscar_dados()
   cotacao = valorEmReal * valorAtualDolar
   return cotacao

    