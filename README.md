Baseado em um sistema de taxação de produtos importados, esse programa simula um calculo de um sistema de tributos. Foram usados dois impostos fantasia, um por estado que receberá a mercadoria e outro por chegada do produto no país. 

- O primeiro imposto é restrito ao estado em que o comprador descrever no preenchimento do formulário e varia de 7 a 12%.
- O segundo imposto seria o de importação para o país e recebe um valor de 20% se for menor que 50 dólares americanos e 90% se for maior que 50 doláres americanos.

Obs: OS valores foram criados a critério de estudo e não condizem com a realidade.

1 - Módulo conversor_real_dolar

    1.1 - A função buscar_dados() é uma implementação para buscar em uma api um arquivo json que retorna o valor atualizado do dolar no dia.
    1.1 - A função real_para_dolar implementa a conversão de um valor em real e utilizando a função buscar_dados() para buscar o valor da cotação do dolar atual e converter de acordo com o valor fornecido.

2 - Atribuição de tributo 
    2.1 - A função valor_de_tributo_estadual vai adicionar o tributo referente ao preço do produto escolhido, de acordo com o estado em que o comprador estiver, para isso foi criado um dicionário com os valores por cada estado. 
    2.2 - A função valor_tributo_importacao adiciona ao valor do produto uma taxa de acordo com o preço do produto.
    2.3 - A função valor_final_consumidor calcula o valor final da importação do produto, no escopo antigo ela receberia as funções de calcular o valor_de_tributo_estadual e valor_tributo_importacao, mas como houve alguns problemas com integração a função de tributo estadual foi transferida para o valor de tributo final.
3 - Main
    3.1 - Recebe a função de valor_final_consumidor para validação dos dados cedidos pelo usuário.