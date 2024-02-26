def sortchip(qtd_inicial, qtd_desejada):
    result = 0

    if qtd_inicial == qtd_desejada:
        result += 1

    elif (qtd_inicial < qtd_desejada) or (qtd_inicial%3 != 0):
        result += 0

    else:
        result += sortchip((qtd_inicial//3)*2, qtd_desejada)
        result += sortchip(qtd_inicial//3, qtd_desejada)

    return result

n = int(input())

for i in range(n):
    qtd = input().split(' ')
    qtd_inicial = int(qtd[0])
    qtd_desejada = int(qtd[1])
    
    if sortchip(qtd_inicial, qtd_desejada) > 0:
        print('SIM')
    else:
        print('NAO')