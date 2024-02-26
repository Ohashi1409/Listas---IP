vida_dolly = int(input())
ataque_dolly = int(input())
defesa_dolly = int(input())
qtd_barriguinha_mole = int(input())
lista_inimigos = []
lista_inimigos_derrotados = []

if (qtd_barriguinha_mole == 0):
    print('Oba! Sem intercorrências pelo caminho! Podemos ir para o carnaval em paz!')
else:
    print('Oh não! Eles querem acabar com o meu Dollynho!')
    for inimigo_dolly in range(qtd_barriguinha_mole):
        nome_inimigo = input()
        vida_inimigo = int(input())
        ataque_inimigo = int(input())
        defesa_inimigo = int(input())
        lista_inimigos.append({'nome': nome_inimigo, 'vida': vida_inimigo, 'ataque': ataque_inimigo, 'defesa': defesa_inimigo})

    for battles in range(len(lista_inimigos)):
        inimigo = lista_inimigos[battles]
        while inimigo['vida'] > 0 and vida_dolly > 0:
            inimigo['vida'] -= (ataque_dolly - inimigo['defesa'])
            if inimigo['vida'] <= 0:
                print(f"O {inimigo['nome']} foi derrotado!")
                print('STATUS DOLLY')
                print(f'Vida: {vida_dolly}')
                lista_inimigos_derrotados.append(inimigo['nome'])
                if len(lista_inimigos_derrotados) == len(lista_inimigos):
                    print('OBA! Dolly venceu todos os inimigos!')
            else:
                vida_dolly -= (inimigo['ataque'] - defesa_dolly)
                if vida_dolly <= 0:
                    print('Que tristeza! Dollynho se foi!')
                    print('Infelizmente Dollynho não conseguiu vencer todos os Barriguinhas Moles…')
                    print(f'Pelo menos levou {len(lista_inimigos_derrotados)} baderneiros com ele!')