escolas_validas = ("Porto da Pedra", "Beija-flor", "Salgueiro", "Grande Rio", "Unidos da Tijuca", "Imperatriz", "Mocidade", "Portela", "Vila Isabel", "Mangueira", "Paraíso do Tuiuti", "Viradouro")
dicionario_escolas = {}
sort_escolas = {}
escolas_input = ''

while escolas_input != 'Fim':
    escolas_input = input()

    if escolas_input != 'Fim':
        escolas_de_samba = tuple(escolas_input.split(': '))
        nome_escola = escolas_de_samba[0]
        nota_escola = escolas_de_samba[1]

        if nome_escola not in escolas_validas:
            print('Epa, o que essa escola está fazendo aqui?!')
        else:
            if nome_escola not in dicionario_escolas.keys():
                print(f'{nome_escola} teve sua nota apurada!')
            else:
                print(f'{nome_escola} teve sua nota atualizada!')
            dicionario_escolas.update({nome_escola: nota_escola})

print('')
sort_escolas = sorted(dicionario_escolas.items(), key = lambda x:x[1], reverse = True)

print('CLASSIFICAÇÃO DO CARNAVAL 2024:')
position = 1
for escolas in sort_escolas:
    print(f'{position}. {escolas[0]}: {escolas[1]}')
    position+=1

print('')
print(f'É CAMPEÃ! A ESCOLA {sort_escolas[0][0]} É A GRANDE VENCEDORA DO CARNAVAL DE 2024, FAZENDO {sort_escolas[0][1]} PONTOS!!')
print(f'Infelizmente, a escola {sort_escolas[-1][0]} não alcançou as expectativas, fazendo apenas {sort_escolas[-1][1]} pontos, e foi rebaixada.')