computadores_disponiveis = int(input())
dinheiro_disponivel = int(input())
tempo_limite = int(input())
quantidade_de_amigos = 0
amigos_validos = True

while(amigos_validos):
    nome = input()
    if nome == "end" :
      amigos_validos = False
    elif ((nome != "laura") and (nome != "carlos") and (nome != "roberto")) :
        quantidade_de_amigos += 1
        if quantidade_de_amigos >= computadores_disponiveis :
          amigos_validos = False
  
#a variável tem igresso começa com false pois ainda não temos nenhum ingresso 
tem_ingresso = False
ingressos_possiveis = 0

if (quantidade_de_amigos > 0):
  print(f"Bom começo! Consegui {quantidade_de_amigos} amigos que podem me ajudar a comprar o ingresso")
  for i in range(1, quantidade_de_amigos+1):
    amigo_ajudando = True
    while (amigo_ajudando):
      valor_ingresso = int(input())
      local_show = input()
      if (local_show == "end"):
        amigo_ajudando = False
      elif ((local_show == "rio de janeiro") or (local_show == "são paulo") or (local_show == "buenos aires")):
        print("Consegui um ingresso em um local que João possa ir! Agora temos que ver o preço")
        amigo_ajudando = False
        if (dinheiro_disponivel >= valor_ingresso):
          print("Consegui o dinheiro! Agora só falta ver a minha colocação na fila dos ingressos...")
          posicao_fila = int(input())
          if (posicao_fila <= (tempo_limite*(6*16))):
            print("ISSOOO, conseguimos um ingresso!!!")
            ingressos_possiveis += 1

            #o not aqui foi utilizado pra transformar o tem_ingresso de false em true,fazendo com que o código fosse rodado
            # e logo após isso, ele receberia o valor True e chegaria novamente no IF, onde dessa vez seria um False após a
            # transformação, o que faria com que o tem_ingresso não mais entrasse no IF e sim no ELSE a partir de agr 
            if (not tem_ingresso):
              tem_ingresso = True
              computador_escolhido = i
              posicao_escolhida = posicao_fila
            else:
                if (posicao_fila < posicao_escolhida):
                    computador_escolhido = i
                    posicao_escolhida = posicao_fila 
          else:
            print(f"Caramba, essa foi quase! Mas infelizmente não consegui um bom lugar na fila dos ingressos no computador de número {i}")
        else:
          print("Caramba! Só tinha ingresso para a pista vip, que está bem acima do meu orçamento.")
  if (tem_ingresso):
    print(f"Consegui o ingresso! Com {int((ingressos_possiveis/quantidade_de_amigos)*100)}% de aproveitamento da ajuda dos meus amigos. E a fila escolhida para comprar o ingresso foi do computador número {computador_escolhido}. Rumo ao show da Taylor!!!")
  elif ((not tem_ingresso) and (quantidade_de_amigos >= computadores_disponiveis/2)):
    print("Não acredito que tive amigos para ocuparem mais da metade dos computadores, e ainda assim não consegui um ingresso...")
  else:
    print("Poxa, não acredito que não consegui o ingresso, acho que eu devia ter chamado mais amigos para ajudar.")
else:
  print("Ah não! João não conseguiu nenhum amigo que o ajudasse. Agora ele vai ter que contar com a sorte para pegar um bom lugar na fila, usando apenas seu computador.")