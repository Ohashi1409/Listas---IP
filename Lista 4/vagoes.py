lista_peso_malas = input().split(', ')
parametros = input().split(', ')
lista_funcionarios = input().split(', ')
horario = input().split(':')
horario = int(''.join(horario))
roteiro = input()


def protocolo_de_inicio():
    organizar_malas(lista_peso_malas)
    funcao_parametros()
    turno()


def organizar_malas(peso_malas) :
    peso_malas = sorted(peso_malas)
    peso_malas[0], peso_malas[-1] = peso_malas[-1], peso_malas[0]
    peso_malas[1], peso_malas[-2] = peso_malas[-2], peso_malas[1]
    print(f"A nova organização das malas é a seguinte: {', '.join(peso_malas)}")
    return peso_malas


def funcao_parametros() :
    blocos_carvao = int(parametros[0])
    peso = int(parametros[1])
    num_passengers = int(parametros[-1])
    velocidade = int((blocos_carvao + 200)/2)
    carga = int((peso+4000)/1000)
    total_pessoas = num_passengers+40
    print(f"A velocidade que o trem partirá é de: {velocidade}Km/H")
    print(f"A carga do Trem em Toneladas é: {carga} Ton.")
    print(f"A quantidade de passageiros é de {total_pessoas}")


def turno():
    lista_convocados = []
    if 700 < horario < 2100 :
        if roteiro == "Roteiro 1":
            lista_convocados.append(lista_funcionarios[0])
            lista_convocados.append(lista_funcionarios[1])
        elif roteiro == "Roteiro 2":
            lista_convocados.append(lista_funcionarios[0])
            lista_convocados.append(lista_funcionarios[-1])
        print(f"Os funcionários convocados são: {', '.join(lista_convocados)}")
    else :
        if roteiro == "Roteiro 1":
            lista_convocados.append(lista_funcionarios[2])
            print(f"Os funcionários convocados são: {', '.join(lista_convocados)}")
        elif roteiro == "Roteiro 2":
            print(f'Os funcionários convocados são: Nenhum! O turno da Madrugada vai ser tranquilo para todos')


protocolo_de_inicio()
