#definindo função pra printar a matriz repetidas vezes
def printando_mapa(matriz):
    for linha in range(8):
        for coluna in range(8):
            if coluna < 7:
                print(matriz[linha][coluna], end = ' ')
            else:
                print(matriz[linha][coluna])

    if not percy_win and not clarisse_win:
        print()


#definindo a movimentação de clarisse
def movimentacao_clarisse(matriz, percyY, percyX):
    global percy_win
    global clarisse_win
    clarisseY = 0
    clarisseX = 0
    mapa = matriz

    for linha in matriz:
        if 'C' in linha:
            clarisseY = matriz.index(linha)
            clarisseX = linha.index('C')

    if clarisseX == percyX:
        if clarisseY > percyY:
            if mapa[clarisseY - 1][clarisseX] == '-':
                mapa[clarisseY - 1][clarisseX] = 'C'
                mapa[clarisseY][clarisseX] = '-'

            elif mapa[clarisseY - 1][clarisseX] == 'A':
                percy_win = True
                mapa[clarisseY - 1][clarisseX] = 'C'
                mapa[clarisseY][clarisseX] = '-'
                print('Vitória!! Nunca subestime o cabeça de alga!')
                printando_mapa(mapa)

            elif mapa[clarisseY - 1][clarisseX] == 'P':
                clarisse_win = True
                mapa[clarisseY - 1][clarisseX] = 'C'
                mapa[clarisseY][clarisseX] = '-'
                print('Ah não, Annabeth vai me matar...')
                printando_mapa(mapa)

        elif clarisseY < percyY:
            if mapa[clarisseY + 1][clarisseX] == '-':
                mapa[clarisseY + 1][clarisseX] = 'C'
                mapa[clarisseY][clarisseX] = '-'

            elif mapa[clarisseY + 1][clarisseX] == 'A':
                percy_win = True
                mapa[clarisseY + 1][clarisseX] = 'C'
                mapa[clarisseY][clarisseX] = '-'
                print('Vitória!! Nunca subestime o cabeça de alga!')
                printando_mapa(mapa)

            elif mapa[clarisseY + 1][clarisseX] == 'P':
                clarisse_win = True
                mapa[clarisseY + 1][clarisseX] = 'C'
                mapa[clarisseY][clarisseX] = '-'
                print('Ah não, Annabeth vai me matar...')
                printando_mapa(mapa)

    elif clarisseX > percyX:
        if mapa[clarisseY][clarisseX - 1] == '-':
            mapa[clarisseY][clarisseX - 1] = 'C'
            mapa[clarisseY][clarisseX] = '-'
        
        elif mapa[clarisseY][clarisseX - 1] == 'A':
            percy_win = True
            mapa[clarisseY][clarisseX - 1] = 'C'
            mapa[clarisseY][clarisseX] = '-'
            print('Vitória!! Nunca subestime o cabeça de alga!')
            printando_mapa(mapa)

        elif mapa[clarisseY][clarisseX - 1] == 'P':
            clarisse_win = True
            mapa[clarisseY][clarisseX - 1] = 'C'
            mapa[clarisseY][clarisseX] = '-'
            print('Ah não, Annabeth vai me matar...')
            printando_mapa(mapa) 

    elif clarisseX < percyX:
        if mapa[clarisseY][clarisseX + 1] == '-':
            mapa[clarisseY][clarisseX + 1] = 'C'
            mapa[clarisseY][clarisseX] = '-'
        
        elif mapa[clarisseY][clarisseX + 1] == 'A':
            percy_win = True
            mapa[clarisseY][clarisseX + 1] = 'C'
            mapa[clarisseY][clarisseX] = '-'
            print('Vitória!! Nunca subestime o cabeça de alga!')
            printando_mapa(mapa)

        elif mapa[clarisseY][clarisseX + 1] == 'P':
            clarisse_win = True
            mapa[clarisseY][clarisseX + 1] = 'C'
            mapa[clarisseY][clarisseX] = '-'
            print('Ah não, Annabeth vai me matar...')
            printando_mapa(mapa)  

    return mapa 


#definindo a movimentação geral de percy
def movimentacao_percy(matriz, direcao, percyY, percyX):
    global percy_win
    global clarisse_win
    global percy_com_bandeira

    mapa = matriz

    if not percy_win and not clarisse_win:
        if direcao == 'cima':
            if mapa[percyY - 1][percyX] == '-':
                if percy_com_bandeira:
                    if (percyY - 1) != 0:
                        print('Agora eu só preciso meter o pé daqui!')

                else :
                    print('Preciso pegar aquela maldita bandeira vermelha.')
                    
                mapa[percyY - 1][percyX] = 'P'
                mapa[percyY][percyX] = '-'

            elif mapa[percyY - 1][percyX] == 'A':
                print('Sinto o poder de Poseidon em minhas veias!')
                mapa[percyY][percyX] = '-'

                if mapa[percyY - 2][percyX] == '-':
                    mapa[percyY - 2][percyX] = 'P'
                    if percy_com_bandeira:
                        if (percyY - 1) != 0:
                            print('Agora eu só preciso meter o pé daqui!')
                    else:
                        print('Preciso pegar aquela maldita bandeira vermelha.')

                elif mapa[percyY - 2][percyX] == 'B':
                    print('Isso! Consegui a bandeira!')
                    percy_com_bandeira = True
                    mapa[percyY - 2][percyX] = 'P'

                else:
                    print('Ah não, Annabeth vai me matar...')
                    clarisse_win = True

            elif mapa[percyY - 1][percyX] == 'B':
                print('Isso! Consegui a bandeira!')
                percy_com_bandeira = True
                mapa[percyY - 1][percyX] = 'P'
                mapa[percyY][percyX] = '-'

        elif direcao == 'baixo':
            if mapa[percyY + 1][percyX] == '-':
                if percy_com_bandeira:
                        print('Agora eu só preciso meter o pé daqui!')
                else:
                        print('Preciso pegar aquela maldita bandeira vermelha.')

                mapa[percyY + 1][percyX] = 'P'
                mapa[percyY][percyX] = '-'

            elif mapa[percyY + 1][percyX] == 'A':
                print('Sinto o poder de Poseidon em minhas veias!')
                mapa[percyY][percyX] = '-'

                if mapa[percyY + 1][percyX] == '-':
                    mapa[percyY + 2][percyX] = 'P'
                    if percy_com_bandeira:
                        print('Agora eu só preciso meter o pé daqui!')
                    else:
                        print('Preciso pegar aquela maldita bandeira vermelha.')

                elif mapa[percyY + 2][percyX] == 'B':
                    print('Isso! Consegui a bandeira!')
                    percy_com_bandeira = True
                    mapa[percyY + 2][percyX] = 'P'

                else:
                    clarisse_win = True
                    print('Ah não, Annabeth vai me matar...')

            elif mapa[percyY + 1][percyX] == 'B':
                    print('Isso! Consegui a bandeira!')
                    percy_com_bandeira = True
                    mapa[percyY + 1][percyX] = 'P'
                    mapa[percyY][percyX] = '-'

        elif direcao == 'esquerda':
            if mapa[percyY][percyX - 1] == '-':
                if percy_com_bandeira:
                    if percyY != 0:
                        print('Agora eu só preciso meter o pé daqui!')

                else:
                    print('Preciso pegar aquela maldita bandeira vermelha.')
            
                mapa[percyY][percyX - 1] = 'P'
                mapa[percyY][percyX] = '-'

            elif mapa[percyY][percyX - 1] == 'A':
                print('Sinto o poder de Poseidon em minhas veias!')
                mapa[percyY][percyX] = '-'
                if mapa[percyY][percyX - 2] == '-':
                    mapa[percyY][percyX - 2] = 'P'
                    if percy_com_bandeira:
                        print('Agora eu só preciso meter o pé daqui!')
                    else:
                        print('Preciso pegar aquela maldita bandeira vermelha.')

                elif mapa[percyY][percyX - 2] == 'B':
                    print('Isso! Consegui a bandeira!')
                    mapa[percyY][percyX - 2] = 'P'
                    percy_com_bandeira = True

                else:
                    clarisse_win = True
                    print('Ah não, Annabeth vai me matar...')

            elif mapa[percyY][percyX - 1] == 'B':
                print('Isso! Consegui a bandeira!')
                mapa[percyY][percyX - 1] = 'P'
                mapa[percyY][percyX] = '-'
                percy_com_bandeira = True


        elif direcao == 'direita':
            if mapa[percyY][percyX + 1] == '-':
                if percy_com_bandeira:
                    if percyY != 0:
                        print('Agora eu só preciso meter o pé daqui!')
                else:
                    print('Preciso pegar aquela maldita bandeira vermelha.')

                mapa[percyY][percyX + 1] = 'P'
                mapa[percyY][percyX] = '-'

            elif mapa[percyY][percyX + 1] == 'A':
                print('Sinto o poder de Poseidon em minhas veias!')
                mapa[percyY][percyX] = '-'
                if mapa[percyY][percyX + 2] == '-':
                    mapa[percyY][percyX + 2] = 'P'
                    if percy_com_bandeira:
                        print('Agora eu só preciso meter o pé daqui!')
                    else:
                        print('Preciso pegar aquela maldita bandeira vermelha.')

                elif mapa[percyY][percyX + 2] == 'B':
                    print('Isso! Consegui a bandeira!')
                    percy_com_bandeira = True
                    mapa[percyY][percyX + 2] = 'P'

                else:
                    clarisse_win = True
                    print('Ah não, Annabeth vai me matar...')

            elif mapa[percyY][percyX + 1] == 'B':
                print('Isso! Consegui a bandeira!')
                percy_com_bandeira = True
                mapa[percyY][percyX + 1] = 'P'
                mapa[percyY][percyX] = '-'

    for linha in mapa:
        if 'P' in linha:
            percyY = mapa.index(linha)

    if (percy_com_bandeira and (percyY == 0)) and not clarisse_win:
        percy_win = True
        print('Vitória!! Nunca subestime o cabeça de alga!')

    return mapa                


#coordenadas do percy
percyY = int(input())
percyX = int(input())

#coordenadas da clarisse
clarisseY = int(input())
clarisseX = int(input())

#coordenadas da poça de agua
aguaY = int(input())
aguaX = int(input())

#coordenadas da bandeira
bandeiraY = int(input())
bandeiraX = int(input())

#mapa do campo de batalha
mapa = [['-','-','-','-','-','-','-','-'], ['-','-','-','-','-','-','-','-'], ['-','-','-','-','-','-','-','-'], ['-','-','-','-','-','-','-','-'], ['-','-','-','-','-','-','-','-'], ['-','-','-','-','-','-','-','-'], ['-','-','-','-','-','-','-','-'], ['-','-','-','-','-','-','-','-']]

#organizando posições dos elementos dentro do campo de batalha
mapa[percyY][percyX] = 'P'
mapa[clarisseY][clarisseX] = 'C'
mapa[aguaY][aguaX] = 'A'
mapa[bandeiraY][bandeiraX] = 'B'

#vencedor
percy_win = False
clarisse_win = False

#conseguir a bandeira
percy_com_bandeira = False

#começando o laço de repetição
while not percy_win and not clarisse_win:

    #atualizando a posiçao do percy
    for linha in mapa:
        if 'P' in linha:
            percyY = mapa.index(linha)
            percyX = linha.index('P')

    mapa = movimentacao_clarisse(mapa, percyY, percyX)

    if not percy_win and not clarisse_win:
        direcao = input()
        mapa = movimentacao_percy(mapa, direcao, percyY, percyX)
        printando_mapa(mapa)