qtd_pessoas = int(input())
dict_pessoa_mascara = {}

for i in range(qtd_pessoas):
    input_pessoa = input().split(' -> ')
    mascara = input_pessoa[1].split(': ')

    dict_pessoa_mascara[input_pessoa[0]] = [mascara[0], mascara[1], 0, 0]

trocas_permitidas = int(input())

for keys in dict_pessoa_mascara.keys():
    dict_pessoa_mascara[keys][2] = trocas_permitidas

continua_troca = True

while continua_troca :
    troca = input()
    if (troca == 'FIM'):
        continua_troca = False
    else:
        if 'Evento especial' not in troca:
            if 'Temos máscaras de cor' not in troca:
                troca = troca.split(' <-> ')

                person1 = troca[0]
                person2 = troca[1]
                mask1 = dict_pessoa_mascara[person1][0]
                mask2 = dict_pessoa_mascara[person2][0]

                qtd_trocas1 = dict_pessoa_mascara[person1][2]
                nivel1 = dict_pessoa_mascara[person1][3]

                qtd_trocas2 = dict_pessoa_mascara[person2][2]
                nivel2 = dict_pessoa_mascara[person2][3]

                if (qtd_trocas1 > 0) and (qtd_trocas2) > 0:
                    dict_pessoa_mascara[person1], dict_pessoa_mascara[person2] = dict_pessoa_mascara[person2], dict_pessoa_mascara[person1]

                    dict_pessoa_mascara[person1][2] -= 1
                    dict_pessoa_mascara[person1][3] += 1

                    dict_pessoa_mascara[person2][2] -= 1
                    dict_pessoa_mascara[person2][3] += 1

                else:
                    if (dict_pessoa_mascara[person1][2] == 0) and (dict_pessoa_mascara[person2][2] > 0):
                        print(f'Eita, amigo, tas preso com a {mask1}, visse? Pode trocar mais ela não.')
                    elif (dict_pessoa_mascara[person1][2] > 0) and (dict_pessoa_mascara[person2][2] == 0):
                        print(f'Eita, amigo, tas preso com a {mask2}, visse? Pode trocar mais ela não.')
                    else:
                        mask_prioridade = sorted([mask1, mask2])
                        print(f"Eita, amigo, tas preso com a {mask_prioridade[0]}, visse? Pode trocar mais ela não.")

            else:
                troca = troca.replace('Temos máscaras de cor ', '')
                mask_color = troca.replace('?', '')

                cont_color = 0

                for info in dict_pessoa_mascara.values():
                    if info[1] == mask_color:
                        cont_color += 1

                print(f'Um total de {cont_color} pessoa(s) está(o) com máscara de cor {mask_color}!')

        else:
            chuva_mask = troca.replace('Evento especial!!! Chuva de máscaras -> ', '')
            chuva_mask = chuva_mask.split(': ')

            nova_mask = chuva_mask[0]
            nivel_nova_mask = int(chuva_mask[1])

            beneficiados = []

            for pessoas in dict_pessoa_mascara.keys():
                mask_atual = dict_pessoa_mascara[pessoas][0]

                if ((dict_pessoa_mascara[pessoas][3]%2) != 0) and (dict_pessoa_mascara[pessoas][3] <= nivel_nova_mask):
                    dict_pessoa_mascara[pessoas][0] = nova_mask
                    dict_pessoa_mascara[pessoas][2] = 4
                    dict_pessoa_mascara[pessoas][3] = nivel_nova_mask
                    beneficiados.append(pessoas)

            if len(beneficiados) == 0:
                print('Vixe... Serviu pra nada o evento Chuva de máscaras :/')
            elif len(beneficiados) == 1:
                print(f'Apenas {beneficiados[0]} é que aproveitou mesmo o evento Chuva de máscaras.')
            else:
                print('Arretaaado demais!! Teve um evento maneiro aqui e ', end='')
                for i in range(len(beneficiados)):
                    if i == len(beneficiados) - 1:
                        print(f'{beneficiados[i]}', end=' ')
                    else:
                        print(f'{beneficiados[i]}', end=', ')
                print('foram beneficiados.')

if len(dict_pessoa_mascara) > 0:
    dict_ordenado = dict(sorted(dict_pessoa_mascara.items()))
    print('Agora é hora de ver quem ficou com que máscara!')
    for position in dict_ordenado:
        print(f'{position} -> {dict_pessoa_mascara[position][0]}: {dict_pessoa_mascara[position][3]}')

    print('Troca de máscaras encerrada! Esperamos que todos tenham se divertido!')