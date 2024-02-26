lista_objetos = input().split(' - ')
objetos_escolhidos = []
comeco_expositor_giratorio = ''

if len(lista_objetos)%2 == 0:
    comeco_expositor_giratorio = lista_objetos[int((len(lista_objetos))/2)]
else :
    comeco_expositor_giratorio = lista_objetos[int((len(lista_objetos))//2)]


objetos_analisados = int(input())
for i in range(objetos_analisados):
    rotacao = input()
    opcao = input()
    direcao = rotacao[-1]
    numero_rotacoes = int(rotacao[:-1])
    if direcao == '>' :
        comeco_expositor_giratorio = ((lista_objetos.index(comeco_expositor_giratorio) + numero_rotacoes)%len(lista_objetos))
    elif direcao == '<' :
        comeco_expositor_giratorio = ((lista_objetos.index(comeco_expositor_giratorio) - numero_rotacoes)%len(lista_objetos))


    if lista_objetos[comeco_expositor_giratorio] in objetos_escolhidos :
        print(f'{lista_objetos[comeco_expositor_giratorio]} já está na mochila. Não seja gananciosa, ou acabará como Midas!')
    else :
        if opcao == "Adicionar":
            objetos_escolhidos.append(lista_objetos[comeco_expositor_giratorio])
            print(f'{lista_objetos[comeco_expositor_giratorio]} adicionado a mochila!')
        elif opcao == "Ignorar":
            print(f'{lista_objetos[comeco_expositor_giratorio]} não vai ser tão útil assim!')

    comeco_expositor_giratorio = lista_objetos[comeco_expositor_giratorio]

if (len(objetos_escolhidos) == 0) or (objetos_escolhidos == [' ']) :
    print('Não achei nada útil no arsenal. Acho que vamos precisar ser menos violentos dessa vez…')
else :
    print('Com ', end='')
    for n in objetos_escolhidos :
        print(n, end=', ')
    print('seremos imbatíveis na caça à bandeira!')