informacoes_deuses = [
    ['Zeus', 'Poseidon', 'Atenas', 'Ares', 'Afrodite'],
    [100, 90, 80, 70, 60],
    ['Raio', 'Tridente', 'Égide', 'Lança', 'Cinto Mágico']
]


sequencia = input()
contador = 1


for i in sequencia :
    i = int(i)
    if i == 0 :
        print(f"Deus:{informacoes_deuses[0][i]}")
        print(f"Poder:{informacoes_deuses[1][i]}")
        print(f"Artefato:{informacoes_deuses[2][i]}")
        if contador != len(sequencia):
            print("")
    elif i == 1 :
        print(f"Deus:{informacoes_deuses[0][i]}")
        print(f"Poder:{informacoes_deuses[1][i]}")
        print(f"Artefato:{informacoes_deuses[2][i]}")
        if contador != len(sequencia) :
            print("")
    elif i == 2 :
        print(f"Deusa:{informacoes_deuses[0][i]}")
        print(f"Poder:{informacoes_deuses[1][i]}")
        print(f"Artefato:{informacoes_deuses[2][i]}")
        if contador != len(sequencia) :
            print("")
    elif i == 3 :
        print(f"Deus:{informacoes_deuses[0][i]}")
        print(f"Poder:{informacoes_deuses[1][i]}")
        print(f"Artefato:{informacoes_deuses[2][i]}")
        if contador != len(sequencia) :
            print("")
    elif i == 4 :
        print(f"Deusa:{informacoes_deuses[0][i]}")
        print(f"Poder:{informacoes_deuses[1][i]}")
        print(f"Artefato:{informacoes_deuses[2][i]}")
        if contador != len(sequencia) :
            print("")


    contador += 1