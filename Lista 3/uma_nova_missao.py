nome_missao = input()
lista_herois = []
heroi = ''
i = 0

while heroi != "Grupo formado" :
    heroi = input()
    lista_herois.append(heroi)

print(f"O grupo formado por {len(lista_herois)-1} heróis para a missão {nome_missao} foi:")
for nome in lista_herois :
    if nome != "Grupo formado" :
        print("-",lista_herois[i])
        i += 1