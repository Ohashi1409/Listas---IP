def menor_que_32(palavra):
    if len(palavra)==32:
        return palavra
    else:
        palavra = '0' + palavra
        palavra = menor_que_32(palavra)
        return palavra


def verificador_tentativa(palavra, byte):
    acertou = False
    nova_palavra = palavra[:8]
    if len(palavra) < 8:
        acertou = False
    elif byte == nova_palavra:
        acertou = True
    else:
        palavra = palavra[1:]
        acertou = verificador_tentativa(palavra, byte)

    return acertou
    

palavra = input()
qtd_tentativas = int(input())
palavra = menor_que_32(palavra)
i = 0

while i < qtd_tentativas:
    byte = input()
    acertou = verificador_tentativa(palavra, byte)
    if not acertou:
        print('Não é essa a senha, estamos ficando sem tempo.')
        i += 1
        if i == qtd_tentativas:
            print('Corre Keanu! Eles nos descobriram!!')
    else:
        print('Muito bem! Estamos dentro! Vamos queimar essa cidade!!')
        i = qtd_tentativas