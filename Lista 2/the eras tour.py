musica = str()
pontuacao = 0
quantidade_de_musicas_tocadas = 0
string_1 = "os fãs estão formando uma ciranda"
string_2 = "os fãs estão ligando os flashes e atrapalhando a visão"
string_3 = "os fãs estão dançando na frente da tela"
string_4 = "os fãs estão gritando o nome da Taylor e atrapalhando a música"
string_5 = "os fãs estão cantando as músicas em coro"
string_6 = "houve um pedido de casamento na sessão"
cont = 0
while pontuacao >= 0 :
    musica = input()
    if musica != "long live" :
        if musica == string_1 :
            pontuacao -= 4
            quantidade_de_musicas_tocadas -= 1
        elif musica == string_2 :
            pontuacao -= 3
            quantidade_de_musicas_tocadas -= 1
        elif musica == string_3 :
            pontuacao -= 3
            quantidade_de_musicas_tocadas -= 1
        elif musica == string_4 :
            pontuacao -= 3
            quantidade_de_musicas_tocadas -= 1
        elif musica == string_5 :
            pontuacao += 1
            quantidade_de_musicas_tocadas -= 1
        elif musica == string_6 :
            pontuacao += 1
            quantidade_de_musicas_tocadas -= 1
        else :
            pontuacao += 1
            quantidade_de_musicas_tocadas += 1
    else :
        print(f"A Taylor conseguiu concluir o show sem muitas interrupções e cantou {quantidade_de_musicas_tocadas} músicas.")
    break
print(f"A Taylor só conseguiu cantar {quantidade_de_musicas_tocadas} músicas e a sessão foi interrompida.")