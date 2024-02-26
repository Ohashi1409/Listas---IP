pontuacao = 0
direcao_escolhida1 = input()
numero_porta = int(input())
opcao1 = str()
opcao2 = str()
opcao3 = str()
opcao4 = str()
opcao5 = str()
if numero_porta % 2 == 0 :
    direcao_certa = "esquerda"
else : 
    direcao_certa = "direita"
if direcao_escolhida1 == direcao_certa :
    pontuacao += 150
    opcao1 = "CERTA"
else :
    pontuacao -= 150
    opcao1 = "ERRADA"
direcao_escolhida2 = input()
cor_porta = input()
planta_porta = input()
forma_macaneta = input()
if (cor_porta == "dourada" or cor_porta == "prateada") or ((planta_porta == "avenca" or planta_porta == "espadinha") and forma_macaneta == "redonda") :
    direcao_certa = "direita"
else : 
    direcao_certa = "esquerda"
if direcao_escolhida2 == direcao_certa :
    pontuacao += 200
    opcao2 = "CERTA"
else : 
    pontuacao -= 200
    opcao2 = "ERRADA"
direcao_escolhida3 = input()
cor_porta = input()
numero_porta = int(input())
planta_porta = input()
forma_macaneta = input()
if ((numero_porta % 5 == 0) and (planta_porta == "espadinha") and (forma_macaneta == "quadrada")) or (cor_porta == "perolada"):
    direcao_certa = "esquerda"
else : 
    direcao_certa = "direita"
if direcao_escolhida3 == direcao_certa :
    pontuacao += 250
    opcao3 = "CERTA"
else : 
    pontuacao -= 250
    opcao3 = "ERRADA"
direcao_escolhida4 = input()
numero_porta = int(input())
if (numero_porta % 3 == 0) and (numero_porta % 2 != 0) and (numero_porta % 5 != 0) :
    direcao_certa = "direita"
else :
    direcao_certa = "esquerda"
if direcao_escolhida4 == direcao_certa :
    pontuacao += 300
    opcao4 = "CERTA"
else :
    pontuacao -= 300
    opcao4 = "ERRADA"
cor_porta = input()
numero_porta = int(input())
planta_porta = input()
flor_lado = input()
forma_macaneta = input()
if (cor_porta == "acobreada") and ((numero_porta % 2 == 1) or (forma_macaneta == "triangular" or forma_macaneta == "quadrada")) and (planta_porta == "jiboia") :
    pontuacao += 500
    opcao5 = "CERTA"
elif (cor_porta == "prateada") and ((flor_lado != "margarida") or (flor_lado != "papoula") or (flor_lado != "cosmos") and ((forma_macaneta == "hexagonal") or (forma_macaneta == "redonda"))) :
    pontuacao += 450
    opcao5 = "CERTA"
elif (cor_porta == "dourada") and ((flor_lado == "lirio") or (flor_lado == "ixora")) and (forma_macaneta == "hexagonal") :
    pontuacao += 400
    opcao5 = "CERTA"
else :
    pontuacao -= 500
    opcao5 = "ERRADA"
print("ARISU, VOCÊ FEZ SUAS ESCOLHAS E AGORA VEREMOS SE ESCOLHEU AS PORTAS CERTAS:")
print(opcao1, opcao2, opcao3, opcao4, opcao5)
if (pontuacao > 0) and ((opcao1 == "ERRADA") or (opcao2 == "ERRADA") or (opcao3 == "ERRADA") or (opcao4 == "ERRADA") or (opcao5 == "ERRADA")) :
    print(f'Você passou com {pontuacao} pontos, mas faça melhores escolhas da próxima vez.')
elif (pontuacao > 0) and ((opcao1 == "CERTA") and (opcao2 == "CERTA") and (opcao3 == "CERTA") and (opcao4 == "CERTA") and (opcao5 == "CERTA")) :
    print(f'Parece que a sorte está ao seu favor, Arisu... Você conseguiu passar com {pontuacao} pontos!')
elif (pontuacao <= 0) and ((opcao1 == "CERTA") or (opcao2 == "CERTA") or (opcao3 == "CERTA") or (opcao4 == "CERTA") or (opcao5 == "CERTA")) :
    print(f'Por mais que você tenha feito escolhas corretas, não foi suficiente para sobreviver. Você finalizou o jogo com {pontuacao} pontos')
elif (pontuacao <= 0) and ((opcao1 == "ERRADA") and (opcao2 == "ERRADA") and (opcao3 == "ERRADA") and (opcao4 == "ERRADA") and (opcao5 == "ERRADA")) :
    print(f'Todas suas escolhas foram erradas, Arisu, esperávamos mais de você... Você será executado pois obteve {pontuacao} pontos.')