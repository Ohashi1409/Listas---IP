def distancia_cidades(x1, y1, x2, y2):
    calculo_distancia = ((x1-x2)**2 + (y1-y2)**2)**0.5

    return calculo_distancia


def cidade_mais_perto(x_noel, y_noel, info_cidade, caminho = []):
    distancia_sem_ordem = []
    distancia_com_ordem = []

    for coordenada_cidade in info_cidade:
        distancia = distancia_cidades(x_noel, y_noel, float(coordenada_cidade[1]), float(coordenada_cidade[2]))

        if (distancia != 0) and (coordenada_cidade[0] not in caminho):
            distancia_sem_ordem.append(distancia)
        else:
            #esse append vai ser somente pra o código não entrar em um elemento que já foi visto
            distancia_sem_ordem.append(2834678.1)

    distancia_com_ordem = sorted(distancia_sem_ordem)
    cidade_mais_perto_index = distancia_sem_ordem.index(distancia_com_ordem[0])

    return cidade_mais_perto_index


def caminho_certo(info_cidade):
    caminho = []
    cidade_mais_perto_index = cidade_mais_perto(0,0, info_cidade)

    for i in range(len(info_cidade)):
        caminho.append(info_cidade[cidade_mais_perto_index][0])
        x_cidade_proxima = float(info_cidade[cidade_mais_perto_index][1])
        y_cidade_proxima = float(info_cidade[cidade_mais_perto_index][2])
        cidade_mais_perto_index = cidade_mais_perto(x_cidade_proxima, y_cidade_proxima, info_cidade, caminho)

    return caminho   


def cifra_de_cesar(codigo, casas_andadas, direcao):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    senha = ''

    for letra in codigo:
        if direcao == 'R':
            senha += alfabeto[(alfabeto.index(letra.lower()) + casas_andadas)%len(alfabeto)]
        elif direcao == 'L':
            senha += alfabeto[(alfabeto.index(letra.lower()) - casas_andadas)%len(alfabeto)]
    
    return senha


qtd_cidades = int(input())
lista_senhas = []
info_cidade = [] 
distancia_sem_ordem = []
distancia_com_ordem = []
lista_nomes_cidades = []
for i in range(qtd_cidades):
    informacoes = input().split(', ')

    if len(informacoes) != 0 and informacoes != [' ']:

        info_cidade.append(informacoes)
        senha = cifra_de_cesar(informacoes[3], int(informacoes[-2]), informacoes[-1]) 
        lista_senhas.append(senha)
        lista_nomes_cidades.append(info_cidade[i][0])

trajetoria = caminho_certo(info_cidade)

for n in range(len(trajetoria)):
    idx = lista_nomes_cidades.index(trajetoria[n])
    print(f'A senha da cidade {info_cidade[idx][0]} é: {lista_senhas[idx].upper()}')