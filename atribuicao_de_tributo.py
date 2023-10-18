

#essa função vai adicionar o tributo referente ao produto
# 1 - calcular o imposto de acordo com o estado
# 2 - calcular o imposto de acordo com o valor do produto
#   2.1 - caso seja acima de 50 dolares, o valor recebe taxação de 92%
#   2.2 - caso seja abaixo de 50 dolares, o valor recebe taxação de 20%
estados = {'Acre':12, 'Alagoas':12, 'Amapá':12,'Amazonas':12, 'Bahia':12, 'Ceará':12,'Distrito Federal':12,'Espírito Santo':12,
              'Goiás':12, 'Maranhão':12, 'Mato Grosso':12, 'Mato Grosso do Sul':12,'Minas Gerais':7,'Pará':12,'Paraíba':12,
              'Paraná':12,'Pernambuco':12,'Piauí':12,'Rio de Janeiro':7,'Rio Grande do Norte':12,'Rio Grande do Sul':7,
              'Rondônia':12,'Roraima':12,'Santa Catarina':7,'São Paulo':7,'Sergipe':12,'Tocantins':12}

def valor_de_tributo(estado):
    valor = 600
    tributo = 0
    for nomes_dos_estados, valor_de_icms in estados.items():
        if nomes_dos_estados == estado:
            tributo = float((valor_de_icms * valor) / 100)
            return tributo

print(valor_de_tributo('Rio de Janeiro'))