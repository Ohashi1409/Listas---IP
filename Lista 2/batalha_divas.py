n = int(input())
nota_coreografia_taylor = 0
nota_figurino_taylor = 0
nota_coreografia_beyonce = 0
nota_figurino_beyonce = 0
equipe_taylor = 0
equipe_beyonce = 0
rep = True
print("Vai começar! Vamos ver quem é a verdadeira diva!")
for i in range (1,n+1) :
    x = i
    nota_coreografia_taylor = 0
    nota_figurino_taylor = 0
    nota_coreografia_beyonce = 0
    nota_figurino_beyonce = 0
    diferenca_pontos = 0
    if rep == True :
        nota_coreografia_taylor = int(input())
        nota_figurino_taylor = int(input())
        nota_coreografia_beyonce = int(input())
        nota_figurino_beyonce = int(input())
        nota_final_taylor = ((nota_coreografia_taylor*4) + (nota_figurino_taylor*3))
        nota_final_beyonce = ((nota_coreografia_beyonce*4) + (nota_figurino_beyonce*3))
        print(f"Vai começar a {x}º rodada!")
        if (nota_final_taylor > nota_final_beyonce) :
            cantora_vencedora = "Tay"
            equipe_taylor += 1
            diferenca_pontos = nota_final_taylor - nota_final_beyonce
            print(f"Fim da apresentação! O placar da rodada {x} foi {nota_final_taylor}x{nota_final_beyonce} para os representantes da {cantora_vencedora}.")
            if diferenca_pontos > 20 :
                print(f"A diferença na pontuação foi de {diferenca_pontos} pontos.")
            else :
                print(f"A diferença de pontos foi de apenas {diferenca_pontos}.")
        else : 
            cantora_vencedora = "Bey"
            equipe_beyonce += 1
            diferenca_pontos = nota_final_beyonce - nota_final_taylor
            print(f"Fim da apresentação! O placar da rodada {x} foi {nota_final_beyonce}x{nota_final_taylor} para os representantes da {cantora_vencedora}.")
            if diferenca_pontos > 20 :
                print(f"A diferença na pontuação foi de {diferenca_pontos} pontos.")
            else :
                print(f"A diferença de pontos foi de apenas {diferenca_pontos}.")
        if (equipe_taylor == 3) :
            print(f"Uuuh! Por um placar de {equipe_taylor} a {equipe_beyonce}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!")
            rep = False 
        elif (equipe_beyonce == 3) :
            print(f"Minha nossa! A equipe da Beyoncé chocou o mundo e venceu a equipe da Taylor Swift por um placar de {equipe_beyonce} a {equipe_taylor}. A Bey é a verdadeira rainha do pop!")
            rep = False
if (equipe_taylor > equipe_beyonce) and (equipe_taylor < 3) :
    print(f"Uuuh! Por um placar de {equipe_taylor} a {equipe_beyonce}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!")
elif (equipe_beyonce > equipe_taylor) and (equipe_beyonce < 3) :
    print(f"Minha nossa! A equipe da Beyoncé chocou o mundo e venceu a equipe da Taylor Swift por um placar de {equipe_beyonce} a {equipe_taylor}. A Bey é a verdadeira rainha do pop!")