#verificando disponibilidade de espaço no inventário pros itens e determinando sua posição
def posicao_inventario(list_inventario, list_posicao, pos_lin, pos_col):
    contador = 0 
    if((pos_col+int(list_posicao[1])-1 == len(list_inventario) or (int(list_posicao[0]) > len(list_inventario[1]) or int(list_posicao[1]) > len(list_inventario[0])))):
        return [-1, -1]
    
    else:
        for posicao_Y in range(int(list_posicao[1])):
            for posicao_X in range(int(list_posicao[0])):
                if list_inventario[posicao_Y + pos_col][posicao_X + pos_lin] == 'O':
                    contador += 1

        if contador == int(list_posicao[0])*int(list_posicao[1]):
            return [pos_col, pos_lin]
        else:
            if (pos_lin + int(list_posicao[0]) == len(list_inventario[0])):
                pos_lin = 0
                pos_col+=1
            else:
                pos_lin+=1

            return posicao_inventario(list_inventario, list_posicao, pos_lin, pos_col)


#verificando quais classes de itens já existem em nosso inventário para não haver repetição
def verificador_inventario(acessorios_necessarios):
    for y in range(len(matriz_inventario)):
        for x in range(len(matriz_inventario[0])):
            for classes in acessorios_necessarios:
                if matriz_inventario[y][x] == classes[0].upper():
                    acessorios_necessarios.remove(classes)
    
    return acessorios_necessarios

#parametros
matriz_inventario = []
itens_adicionados = []
equipamentos = []
inventario = 0

#matriz do inventario
while inventario != 'finalizar':
    inventario = input()

    if inventario != 'finalizar':

        matriz_inventario.append(list(inventario))

#recebendo que tipos de item são necessários
acessorios_necessarios = input().split(', ')
acessorios_necessarios = verificador_inventario(acessorios_necessarios)

#recebendo os equipamentos e printando as frases caso possamos ou não adicionar algum elemento
while equipamentos != 'finalizar programa':
    equipamentos = input()

    if equipamentos != 'finalizar programa':
        equipamentos = equipamentos.split('-')
        nome_item = equipamentos[0]
        tamanho_item = equipamentos[1].split('x')
        classe_item = equipamentos[2]

        if classe_item not in acessorios_necessarios:
            print(f'Não precisamos de {nome_item}')
        else:
            posicao_item = posicao_inventario(matriz_inventario, tamanho_item, 0, 0)
            if posicao_item == [-1, -1]:
                print(f'Não há espaço para {nome_item}')
            else:
                print(f'Item adicionado: {nome_item}')
                for y in range(int(tamanho_item[0])):
                    for x in range(int(tamanho_item[1])):
                       matriz_inventario[x+posicao_item[0]][y+posicao_item[1]] = classe_item[0].upper()
                acessorios_necessarios.remove(classe_item)

#print matriz
for x in range(len(matriz_inventario)):
    print(''.join(matriz_inventario[x]))
            
#print dos itens faltosos(caso haja)
if len(acessorios_necessarios) > 0:
    print(f'Faltou: {", ".join(acessorios_necessarios)}')