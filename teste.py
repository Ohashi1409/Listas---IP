def chave_por_valor(candidatos, valor_requerido):
    for chave, valor in candidatos.items():
        if candidatos[chave]["fantasia"] == valor_requerido:
            return chave
    return None
 
def ordenar_por_nota(candidatos):
    return sorted(candidatos.items(), key=lambda x: x[1]['nota'], reverse=True)
 
def remover_candidato(candidatos, nome):
    if nome not in candidatos:
        print(f"Hmmm não consegui achar {nome} no banco de dados...")
    else:
        print(f"Parece que {nome} desistiu...")
        candidatos.pop(nome)
    return True
 
def adicionar_candidato(candidatos, nome, fantasia):
    if nome in candidatos:
        print(f'Opa, parece que {nome} ja consta aqui, voce quis dizer "Atualizar"?')
        return False
    else:
        if fantasia in [f['fantasia'] for f in candidatos.values()]:
            candidato_com_fantasia = chave_por_valor(candidatos, fantasia)
            print(f"Eita, parece que {nome} tentou usar a fantasia {fantasia} que ja está sendo "
                f"utilizada por {candidato_com_fantasia}, ele deverá ser desqualificado por plágio")
            return False
        else: 
            modificar_candidatos(candidatos, nome, fantasia)
            print(f"{nome} é o novo participante do desfile!")
            return True
    return None
 
def previa(candidatos):
    if len(candidatos) > 0:
        candidatos = dict(sorted(candidatos.items()))
        participantes_por_nota = ordenar_por_nota(candidatos)
        diferenca = round((participantes_por_nota[0][1]["nota"] - participantes_por_nota[1][1]["nota"]),1)
        print(f"Até o momento, o primeiro colocado é {list(dict(participantes_por_nota).keys())[0]} com uma "
            f"diferença de {diferenca} pontos para o segundo colocado")
    return True
 
def atualizar_candidatos(candidatos, nome, fantasia):
    if nome not in candidatos:
        print(f"Hmmm não consegui achar {nome} no banco de dados...")
        return False
    else:
        if fantasia in [f['fantasia'] for f in candidatos.values()]:
            candidato_com_fantasia = chave_por_valor(candidatos, fantasia)
            print(f"Eita, parece que {nome} tentou usar a fantasia {fantasia} que ja está sendo "
                f"utilizada por {candidato_com_fantasia}, ele deverá ser desqualificado por plágio")
            if nome in candidatos:
                candidatos.pop(nome)
            return False
        else: 
            modificar_candidatos(candidatos, nome, fantasia)
            print(f"Fantasia de {nome} atualizada")
            return True
 
 
def modificar_candidatos(candidatos, nome, fantasia):
    radicando = 1; indice = 0
    candidatos[nome] = {"fantasia": fantasia, "nota": 0}
    for r in fantasia.lower():
        if r not in vogais and r != " ":
            radicando = radicando*alfabeto[r]
            indice += 1
 
    if radicando and indice !=0:
        x = (radicando ** (1/indice))
        if x != 0:
            nota = (len(fantasia)**2 /x)
            candidatos[nome]["nota"] = nota
        return True
    else:
        candidatos.pop(nome)
    return False
 
 
alfabeto = {chr(l):l-96 for l in range(97,123)}
candidatos = {}; entrada = ''; participantes_por_nota = []
vogais = ["a", "e", "i", "o", "u"]
 
while entrada != "Fim do desfile":
    entrada = input()
    if entrada != "Fim do desfile":
        if entrada == "Remover":
            nome = input()
            remover_candidato(candidatos, nome)
 
        elif entrada == "Julgar previamente":
            previa(candidatos)
 
        elif entrada == "Adicionar":
            nome, fantasia = input().split(" - ")
            adicionar_candidato(candidatos, nome, fantasia)
 
        elif entrada == "Atualizar":
            nome, fantasia = input().split(" - ")
            atualizar_candidatos(candidatos, nome, fantasia)
 
 
if len(candidatos) == 0:
    print("=== RESULTADOS DO DESFILE ===")
 
if len(candidatos) != 0:
    candidatos = dict(sorted(candidatos.items()))
    candidatos = dict(ordenar_por_nota(candidatos))
    print("=== RESULTADOS DO DESFILE ===")
    n = 1
    for i in candidatos:
        print(f"{n}. {i} --- {round(candidatos[i]['nota'],1)}")
        print()
        n += 1
    if len(candidatos) > 0:
        print(f"PARABÉNS {(list(candidatos.keys())[0]).upper()}!!! VOCÊ ACABA DE VENCER O PRIMEIRO DESFILE DO LIMOEIRO!!")
    else:
        print("Parece que não sobrou ninguém na disputa, que pena...")
else:
    print("Parece que não sobrou ninguem na disputa, que pena…")