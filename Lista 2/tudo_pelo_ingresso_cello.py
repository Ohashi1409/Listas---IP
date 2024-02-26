computadores_disponiveis = int(input())
dinheiro_disponivel = float(input())
tempo_espera_limite = int(input())

qnt_amigos = 0
listar_amigos = True
while(listar_amigos):
  nome_amigo = input()
  if(nome_amigo == "end"):
    listar_amigos = False
  elif(nome_amigo != "laura" and nome_amigo != "carlos" and nome_amigo != "roberto"):
    qnt_amigos += 1
    if(qnt_amigos >= computadores_disponiveis):
      listar_amigos = False

ingressos = 0
tem_ingresso = False
if(qnt_amigos > 0):
  print(f"Bom começo! Consegui {qnt_amigos} amigos que podem me ajudar a comprar o ingresso")
  for amigo in range(1, qnt_amigos+1):
    amigo_ajudando = True
    while (amigo_ajudando):
      valor_do_ingresso = float(input())
      local_do_show = input()
      if(local_do_show == "end"):
        amigo_ajudando = False
      elif(local_do_show == "rio de janeiro" or local_do_show == "são paulo" or local_do_show == "buenos aires"):
        print("Consegui um ingresso em um local que João possa ir! Agora temos que ver o preço")
        amigo_ajudando = False
        if(valor_do_ingresso <= dinheiro_disponivel):
          print("Consegui o dinheiro! Agora só falta ver a minha colocação na fila dos ingressos...")
          posicao_fila = int(input())
          if(posicao_fila <= tempo_espera_limite*6*16):
            print("ISSOOO, conseguimos um ingresso!!!")
            ingressos += 1
            if(not tem_ingresso):
              tem_ingresso = True
              computador_escolhido = amigo
              posicao_escolhida = posicao_fila
            else:
                if(posicao_fila < posicao_escolhida):
                    computador_escolhido = amigo
                    posicao_escolhida = posicao_fila 
          else:
            print(f"Caramba, essa foi quase! Mas infelizmente não consegui um bom lugar na fila dos ingressos no computador de número {amigo}")
        else:
          print("Caramba! Só tinha ingresso para a pista vip, que está bem acima do meu orçamento.")
  if(tem_ingresso):
    print(f"Consegui o ingresso! Com {int((ingressos/qnt_amigos)*100)}% de aproveitamento da ajuda dos meus amigos. E a fila escolhida para comprar o ingresso foi do computador número {computador_escolhido}. Rumo ao show da Taylor!!!")
  elif(not tem_ingresso and qnt_amigos >= computadores_disponiveis/2):
    print("Não acredito que tive amigos para ocuparem mais da metade dos computadores, e ainda assim não consegui um ingresso...")
  else:
    print("Poxa, não acredito que não consegui o ingresso, acho que eu devia ter chamado mais amigos para ajudar.")
else:
  print("Ah não! João não conseguiu nenhum amigo que o ajudasse. Agora ele vai ter que contar com a sorte para pegar um bom lugar na fila, usando apenas seu computador.")