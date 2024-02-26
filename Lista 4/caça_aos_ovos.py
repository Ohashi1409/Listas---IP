def maximo(a, b) :
    if a >= b :
        return a
    else :
        return b


qtd_dias = int(input())
total_ovos_encontrados = 0
total_ovos_escondidos = 0

for i in range(1, qtd_dias+1) :
    ovos_encontrados_dia = 0
    ovos_escondidos_dia = int(input())
    horoscopo_dia = input()
    if horoscopo_dia == "Os astros estão radiantes hoje! Eles farão o possível para abençoar a todos com boa sorte.":
        ovos_encontrados_dia = int(ovos_escondidos_dia)
    elif horoscopo_dia == "Os astros estão de bom humor hoje. Acho que você terá um pouco de sorte extra." :
        ovos_encontrados_dia = int(ovos_escondidos_dia*0.7)
    elif horoscopo_dia == "As estrelas estão neutras hoje. O dia está em suas mãos.":
        ovos_encontrados_dia = maximo(ovos_escondidos_dia*0.7, ovos_escondidos_dia/((ovos_escondidos_dia%i)+1))
        ovos_encontrados_dia = int(ovos_encontrados_dia)
    elif horoscopo_dia == "Isso é raro. As estrelas estão absolutamente neutras hoje." :
        if (i == 2) and (ovos_escondidos_dia == 1) :
            ovos_encontrados_dia = int(ovos_escondidos_dia%i)
        ovos_encontrados_dia = int((ovos_escondidos_dia%i) + 1)
    elif horoscopo_dia == "Hoje, Kiq não pôde consultar as estrelas. Sem a orientação astrológica, a busca por ovos fica à mercê do destino.":
        ovos_encontrados_dia = 0
    total_ovos_escondidos += ovos_escondidos_dia
    total_ovos_encontrados += ovos_encontrados_dia
    print(f"Dia {i}")
    print(f"Hoje Carlos encontrou {ovos_encontrados_dia} ovos!!")

aproveitamento = float((total_ovos_encontrados/total_ovos_escondidos)*100)
print(f"Kiq encontrou {total_ovos_encontrados} de um total de {total_ovos_escondidos}")
if aproveitamento == 100 :
    print("Incrível! Seu signo está em alta. Você encontrou todos os ovos!")
elif aproveitamento > 66 :
    print("Ótimo trabalho! Os astros estão ao seu lado. Você encontrou a maioria dos ovos!")
elif aproveitamento > 33 :
    print("Bom esforço! Os astros sorriem para você. Muitos ovos foram encontrados.")
elif aproveitamento > 0 :
    print("Continue procurando! Seu horóscopo sugere que há mais ovos a serem encontrados.")
else : 
    print("Ainda não encontrou nenhum ovo. O horóscopo aconselha persistência. Continue tentando!")