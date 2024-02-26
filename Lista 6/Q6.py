comando = ''
dict_pessoas = {}
ranking_fantasias = {}
ranking_fantasias_ordenado = {}
remove = False
deve_eliminar = []
alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
consoantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

def calcula_nota(fantasia):
    len_string = len(fantasia)
    cont_consoante = 0
    denom = 0
    for i in fantasia:
        n = i.lower()
        if n in consoantes:
            if denom == 0:
                denom = alfabeto.index(n) + 1
            else:
                denom *= alfabeto.index(n) + 1
            cont_consoante += 1

    if denom == 0:
        return 0
    else:
        result = ((len_string**2)/((denom)**(1/cont_consoante)))
        return result


while comando != 'Fim do desfile':
    comando = input()
    if comando == 'Julgar previamente':
        remove = False
        candidato_in_rank = []
        for nomes in dict_pessoas.keys():
            nota = calcula_nota(dict_pessoas[nomes])
            if nota == 0:
                remove = True
                deve_eliminar.append(nomes)
            ranking_fantasias[nomes] = nota
            ranking_fantasias = dict(sorted(ranking_fantasias.items()))
            candidato_in_rank = list(sorted(ranking_fantasias, key = lambda x:x[1], reverse=True))
            ranking_fantasias = dict(sorted(ranking_fantasias.items(), key=lambda x: x[1], reverse=True))
        if remove:
            for i in deve_eliminar:
                del dict_pessoas[i]
                del ranking_fantasias[i]
                candidato_in_rank.remove(i)
        if len(candidato_in_rank) == 1:
            print(f'Até o momento, o primeiro colocado é {candidato_in_rank[0]} com uma diferença de {nota} pontos para o segundo colocado')
        elif len(candidato_in_rank) > 1:
            nota_diferenca = round(list(ranking_fantasias.values())[0] - list(ranking_fantasias.values())[1], 1)
            print(f'Até o momento, o primeiro colocado é {list(ranking_fantasias.keys())[0]} com uma diferença de {nota_diferenca} pontos para o segundo colocado')

    elif comando != 'Fim do desfile':
        pessoa_fantasia = input().split(' - ')
        if comando == 'Adicionar':
            if pessoa_fantasia[0] in dict_pessoas.keys():
                print(f'Opa, parece que {pessoa_fantasia[0]} ja consta aqui, voce quis dizer "Atualizar"?')
            elif pessoa_fantasia[1] in dict_pessoas.values():
                for keys in dict_pessoas.keys():
                    if dict_pessoas[keys] == pessoa_fantasia[1]:
                        print(f'Eita, parece que {pessoa_fantasia[0]} tentou usar a fantasia {pessoa_fantasia[1]} que ja está sendo utilizada por {keys}, ele deverá ser desqualificado por plágio')
            else:
                dict_pessoas.update({pessoa_fantasia[0]: pessoa_fantasia[1]})
                print(f'{pessoa_fantasia[0]} é o novo participante do desfile!')
        elif comando == 'Remover':
            if pessoa_fantasia[0] not in dict_pessoas.keys():
                print(f'Hmmm não consegui achar {pessoa_fantasia[0]} no banco de dados...')
            else:
                del dict_pessoas[pessoa_fantasia[0]]
                if pessoa_fantasia[0] in ranking_fantasias:
                    del ranking_fantasias[pessoa_fantasia[0]]
                print(f'Parece que {pessoa_fantasia[0]} desistiu...')
        elif comando == 'Atualizar':
            if pessoa_fantasia[0] not in dict_pessoas.keys():
                print(f'Hmmm não consegui achar {pessoa_fantasia[0]} no banco de dados...')
            else:
                if pessoa_fantasia[1] in dict_pessoas.values():
                    for keys in dict_pessoas.keys():
                        if dict_pessoas[keys] == pessoa_fantasia[1]:
                            print(f'Eita, parece que {pessoa_fantasia[0]} tentou usar a fantasia {pessoa_fantasia[1]} que ja está sendo utilizada por {keys}, ele deverá ser desqualificado por plágio')
                    del dict_pessoas[pessoa_fantasia[0]]
                    if pessoa_fantasia[0] in ranking_fantasias:
                        del ranking_fantasias[pessoa_fantasia[0]]
                else:
                    dict_pessoas.update({pessoa_fantasia[0]: pessoa_fantasia[1]})
                    print(f'Fantasia de {pessoa_fantasia[0]} atualizada')

for nomes in dict_pessoas.keys():
    nota = calcula_nota(dict_pessoas[nomes])
    ranking_fantasias[nomes] = nota

for i in sorted(ranking_fantasias, key = ranking_fantasias.get, reverse=True):
    ranking_fantasias_ordenado[i] = ranking_fantasias[i]

if len(ranking_fantasias_ordenado) == 0:
    print('=== RESULTADOS DO DESFILE ===')
    print('Parece que não sobrou ninguem na disputa, que pena…')
else:
    print('=== RESULTADOS DO DESFILE ===')
    cont = 0
    for keys in ranking_fantasias_ordenado.keys():
        print(f'{cont+1}. {keys} --- {ranking_fantasias_ordenado.get(keys):.1f}\n')
        cont += 1

    ranking_fantasias_ordenado = list(ranking_fantasias_ordenado)
    print(f'PARABÉNS {ranking_fantasias_ordenado[0].upper()}!!! VOCÊ ACABA DE VENCER O PRIMEIRO DESFILE DO LIMOEIRO!!')