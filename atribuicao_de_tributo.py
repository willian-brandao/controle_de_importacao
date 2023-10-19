import conversor_real_dolar 
from main import*


estados = {'Acre':12, 'Alagoas':12, 'Amapá':12,'Amazonas':12, 'Bahia':12, 'Ceará':12,'Distrito Federal':12,'Espírito Santo':12,
              'Goiás':12, 'Maranhão':12, 'Mato Grosso':12, 'Mato Grosso do Sul':12,'Minas Gerais':7,'Pará':12,'Paraíba':12,
              'Paraná':12,'Pernambuco':12,'Piauí':12,'Rio de Janeiro':7,'Rio Grande do Norte':12,'Rio Grande do Sul':7,
              'Rondônia':12,'Roraima':12,'Santa Catarina':7,'São Paulo':7,'Sergipe':12,'Tocantins':12}


'''
Essa função recebe o valor do produto convertido em dolar.
IMPORTANTE: O valor inserido pelo usuário será em real, então o cálculo final terá que ser em real!

'''
def valor_tributo_importacao(valor):
    tributo_importacao = 0
# converto o valor recebido em real para dolar. ex: 100 -> 19,7
    valor_convertido = conversor_real_dolar.real_para_dolar(valor)
#verificando qual será a taxa de importação do valor recebido, se for maior que 50 = 90% se for menor 20%
    if valor_convertido >= 50:
        tributo_importacao = float((valor * 92)/100)
    else:
        tributo_importacao = float((valor * 20)/ 100)
        
    return tributo_importacao

def valor_final_consumidor(valor, nome_estado):
    
    taxa_importacao = valor_tributo_importacao(valor)
    #taxa_estadual = valor_de_tributo_estadual(nome_estado)
    tributo_icms = 0
    for nomes_estados, valor_icms in estados.items():
        if nomes_estados == nome_estado:
            tributo_icms = float((valor_icms * valor) / 100)
            
    tributo_final = 0 
    tributo_final = valor + tributo_icms+ taxa_importacao
    return tributo_final

'''
def valor_de_tributo_estadual(estado):    
    tributo = 0
    for nomes_dos_estados, valor_de_icms in estados.items():
        if nomes_dos_estados == estado:
            tributo = float((valor_de_icms * valor) / 100 )  
            return tributo


def valor_final_consumidor(valor, nome_estado):
    
    taxa_importacao = valor_tributo_importacao(valor)
    taxa_estadual = valor_de_tributo_estadual(nome_estado)
    
    tributo_final = 0 
    tributo_final = valor + taxa_estadual + taxa_importacao
    return tributo_final
'''
