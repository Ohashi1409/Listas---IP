lista_labirinto = []
labirinto = ''

while labirinto != "Fim do labirinto" :
    labirinto = input()
    lista_labirinto.append(labirinto.split(' '))

linha = 0
coluna = 0

for i in lista_labirinto :
    for n in labirinto :
        if n == 1 :
            print('Bomdia')