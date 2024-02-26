def decodificador(presente, lista):
        presente = ''
        
        for codigo in lista :
            if codigo != '':
                codigo = int(codigo)
                presente += chr(codigo)

        return presente


def presente_valido(soma, lista):
    soma = 0

    for num in lista :
        if num != '':
            num = int(num)
            soma += num

    if (soma%2 != 0) and (presentes_decodificado not in lista_itens_excluidos):
        lista_itens_excluidos.append(presentes_decodificado)
    elif (soma%2 == 0) and (presentes_decodificado not in lista_presentes_anya) and (presentes_decodificado not in lista_itens_excluidos):
        lista_presentes_anya.append(presentes_decodificado)
     

n = int(input())
lista_presentes_anya = []
lista_itens_excluidos = []
soma_codigos = 0

for i in range(n):
    presentes_decodificado = ''
    presentes_anya = input().split(' ')
    presentes_decodificado = decodificador(presentes_decodificado, presentes_anya)
    if (presentes_decodificado in lista_presentes_anya) or (presentes_decodificado in lista_itens_excluidos) :
        print(f'{presentes_decodificado} já está na lista de presentes da Anya!!')
    else:
        print(f'{presentes_decodificado} foi adicionado a lista ultrassecreta de presentes da Anya!!')
    presente_valido(soma_codigos, presentes_anya)

if (len(lista_itens_excluidos) >= 1):
    print(f'Infelizmente o Twilight é mão de vaca e os seguintes itens precisaram ser excluídos da lista de presentes ultrassecretos da Anya: {", ".join(lista_itens_excluidos)}.')
if (len(lista_presentes_anya) == 0 or (lista_presentes_anya == [' '])):
    print('O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!')
elif (len(lista_itens_excluidos) == 0) or (lista_itens_excluidos == [' ']):
    print('Parece que o Dia das Crianças desse ano será especial!!!! Anya ganhará todos os presentes planejados, mesmo que ela não seja tão exemplar como deveria…')
if len(lista_presentes_anya) != 0:
    print(f'Lista final dos melhores presentes da Anya: {", ".join(lista_presentes_anya)}.')