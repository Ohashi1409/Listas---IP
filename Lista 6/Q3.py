preco_ingrediente = {'tomate': 3, 'cebola': 2, 'coentro': 1, 'manteiga': 5.50, 'macaxeira': 3, 
                     'alho': 1.50, 'pimentao': 2, 'azeite': 15, 'camarao': 30, 'carne de sol': 30, 
                     'queijo coalho': 15, 'massa de tapioca': 10, 'leite de coco': 5, 'dende': 15, 
                     'creme de leite': 4, 'moranga': 10}

qtd_ingrediente = {'tomate': 5, 'cebola': 5, 'coentro': 5, 'manteiga': 5, 'macaxeira': 5, 
                   'alho': 5, 'pimentao': 5, 'azeite': 5, 'camarao': 5, 'carne de sol': 5, 
                   'queijo coalho': 5, 'massa de tapioca': 5, 'leite de coco': 5, 'dende': 5, 
                   'creme de leite': 5, 'moranga': 5}

pratos_possiveis = {'bobo de camarao': 58, 'tapioca de carne de sol': 60, 'carne de sol com macaxeira': 38.50, 'camarao na moranga': 68.50}

ingredientes_prato = {'bobo de camarao': ('camarao', 'macaxeira', 'leite de coco', 'dende', 'tomate', 'cebola'), 
                      'tapioca de carne de sol': ('massa de tapioca', 'carne de sol', 'queijo coalho', 'tomate', 'cebola'), 
                      'carne de sol com macaxeira': ('carne de sol', 'macaxeira', 'manteiga'), 
                      'camarao na moranga': ('moranga', 'camarao', 'cebola', 'alho', 'tomate', 'pimentao', 'creme de leite', 'azeite', 'coentro')}

caixa = 30.0
pedidos_dia = ()
pedidos_sem_rep = ()
preco_prato_novo = 0
contador_prato_novo = 0

def comprar_ingredientes(i):
    global caixa
    global preco_ingrediente
    global qtd_ingrediente

    caixa -= (preco_ingrediente[i]*4)
    qtd_ingrediente[i] = 4

def fazer_pedido(qtd_ingrediente, ingredientes_prato, pedido):
    global caixa
    for i in ingredientes_prato[pedido]:
        if qtd_ingrediente[i] > 0:
            qtd_ingrediente[i] -= 1
        else:
            comprar_ingredientes(i)
            qtd_ingrediente[i] -= 1
    
    return qtd_ingrediente


def mais_pedido(pratos, pedidos_dia):
    rank_pratos = {}
    for p in pratos:
        qtd_pedidos = pedidos_dia.count(p)
        rank_pratos[p] = qtd_pedidos 

    prato_mais_pedido = sorted(rank_pratos, key = rank_pratos.get, reverse = True)
    
    return prato_mais_pedido

pedido = ''
continuar = True
while continuar:
    try:
        pedido = input()
        if pedido in pratos_possiveis:
            print(f'{pedido} saindo...')
            caixa += pratos_possiveis[pedido]
            qtd_vendas_prato = fazer_pedido(qtd_ingrediente, ingredientes_prato, pedido)
            if pedido not in pedidos_sem_rep:
                pedidos_sem_rep += (pedido, )
            pedidos_dia += (pedido, )
        else:
            contador_prato_novo += 1
            if contador_prato_novo < 3:
                print(f'{pedido} ainda não é uma opção disponível.')
            else:
                preco_prato_novo = 0
                contador_prato_novo = 0
                tupla_ingred = ()
                for i in range(9):
                    ingred_novo_prato = input()
                    tupla_ingred += (ingred_novo_prato, )
                    preco_prato_novo += preco_ingrediente[ingred_novo_prato]
                ingredientes_prato[pedido] = tupla_ingred
                preco_prato_novo += 5
                pratos_possiveis[pedido] = preco_prato_novo
                print(f'Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Sabores de Recife.')
    except EOFError:
        continuar = False
        print('##### Fim do expediente #####')
        
prato_mais_pedido = mais_pedido(pedidos_sem_rep, pedidos_dia)

print(f'O lucro obtido no dia de hoje foi de R${float(caixa - 30):.2f}.')
if prato_mais_pedido[0] == 'bobo de camarao':
    print('O bom e tradicional Bobó de Camarão, líder em vendas, nunca será superado!')
else:
    print(f'{prato_mais_pedido[0][0].upper()}{prato_mais_pedido[0][1:]} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário Bobó de Camarão.')