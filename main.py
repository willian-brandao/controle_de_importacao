import atribuicao_de_tributo
import conversor_real_dolar



if __name__ =='__main__':
    print(50*'=')
    print("CALCULADORA DE TAXAS DE IMPORTAÇÃO")
    print(50*"=")
    valor_do_produto  = float(input('Insira o valor do produto: '))
    estado_de_entrega = input('O estado de entrega do produto: ')
    
    calculo_de_tributacao = atribuicao_de_tributo.valor_final_consumidor(valor_do_produto, estado_de_entrega)
    imposto_de_importacao = atribuicao_de_tributo.valor_tributo_importacao(valor_do_produto)
    
    
    print(f"Estado de entrega: ", estado_de_entrega)
    print(f"Imposto de importação:{imposto_de_importacao}\n")
    print(f"Valor a ser pago: R$ {calculo_de_tributacao:,.2f}")
    print(50*"=")
    