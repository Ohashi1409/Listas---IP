def desafio1():
    frase_x = input()
    eh_pangrama = False
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    qtd_vezes_letra_aparece = [0 for _ in range(26)]

    for i in frase_x:
        if i in alfabeto:
            qtd_vezes_letra_aparece[alfabeto.index(i)] += 1

    max_rep = max(qtd_vezes_letra_aparece)
    eh_pangrama = min(qtd_vezes_letra_aparece)!=0

    if eh_pangrama:
        x_noel = max(qtd_vezes_letra_aparece)
    else :
        x_noel = min([max_rep if i == 0 else i for i in qtd_vezes_letra_aparece])

    return x_noel
    

def desafio2():
    palavra_y = input()
    fibonacci = [0]
    num_1 = 0
    num_2 = 1
    proximo_numero = 0
    vogais = ['a', 'e', 'i', 'o', 'u']
    stop = False

    for i in range(len(palavra_y)):
        proximo_numero = num_1 + num_2
        num_1 = proximo_numero
        num_2 = (proximo_numero-num_2)
        fibonacci.append(proximo_numero)

    for i in palavra_y:
        if not stop:
            if i.lower() in vogais:
                y_noel = int((fibonacci[-1])*4)
                stop = True
            else :
                y_noel = int((fibonacci[-1])*2)

    return y_noel


def desafio3():
    palavra_z = input()
    frase_z = input()
    maiusculas_palavra = 0
    minusculas_palavra = 0
    maiusculas_frase = 0
    minusculas_frase = 0

    for i in palavra_z:
        if i == i.upper():
            maiusculas_palavra+=1
        elif i == i.lower():
            minusculas_palavra+=1

    for n in frase_z:
        if n == n.upper():
            if n != ' ':
                maiusculas_frase+=1
        elif n == n.lower():
            if n != ' ':
                minusculas_frase+=1

    calculo_palavra = minusculas_palavra-maiusculas_palavra
    calculo_frase = minusculas_frase-maiusculas_frase
    if calculo_palavra <= 0:
        z_noel = 0
    else:
        z_noel = calculo_frase**calculo_palavra

    return z_noel


coordenada_x_noel = int(desafio1())
coordeanda_y_noel = int(desafio2())
coordenada_z_noel = int(desafio3())
x_jack = int(input())
y_jack = int(input())
z_jack = int(input())

distancia_noel_jack = float(((coordenada_x_noel - x_jack)**2 + (coordeanda_y_noel - y_jack)**2 + (coordenada_z_noel - z_jack)**2)**0.5)

print(f'A 1ª coordenada do Papai Noel é: {coordenada_x_noel}')
print(f'A 2ª coordenada do Papai Noel é: {coordeanda_y_noel}')
print(f'A 3ª coordenada do Papai Noel é: {coordenada_z_noel}')
print(f'A distância entre Jack Esqueleto e Papai Noel é: {distancia_noel_jack:.2f}')