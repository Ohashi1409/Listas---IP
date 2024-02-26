colecao_completa = ["O Ladrão de Raios", "O Mar de Monstros", "A Maldição do Titã", "A Batalha do Labirinto", "O Último Olimpiano"]

colecao_sergio = input().split(", ")
qtd_total_edicoes = int(input())

livros_lidos = 0
livro_nao_lido = []
lista_livro_outra_saga = []

for livro in colecao_sergio :
    if livro not in colecao_completa :
        lista_livro_outra_saga.append(livro)

for livros in colecao_completa :
    if livros in colecao_sergio :
        livros_lidos += 1
    else :
        livro_nao_lido.append(livros)

if livros_lidos == 5 :
    print("Sua coleção está completa! Você pode ler à vontade.")
    if (len(lista_livro_outra_saga) >= 1) and (lista_livro_outra_saga != ['']):
        print(f'Cuidado, Sérgio! Você está organizando seus livros de uma forma errada, o(s) livro(s): ', end = "")
        for n in lista_livro_outra_saga :
            print(n, end= ", ")
        print('não faz(em) parte da saga "Percy Jackson e os Olimpianos".')

elif livros_lidos == 0 :
    print("Caramba, você não tem nenhum livro. Compre todos imediatamente.")
    if (len(lista_livro_outra_saga) >= 1) and (lista_livro_outra_saga != ['']):
        print(f'Cuidado, Sérgio! Você está organizando seus livros de uma forma errada, o(s) livro(s): ', end = "")
        for n in lista_livro_outra_saga :
            print(n, end= ", ")
        print('não faz(em) parte da saga "Percy Jackson e os Olimpianos".')

elif 0 < livros_lidos < 5 :
    print(f"Infelizmente, sua coleção está incompleta. Falta(m) esse(s) livro(s): ", end= "")
    for i in livro_nao_lido :
        if (len(livro_nao_lido) > 1) and (i != livro_nao_lido[-1]) :
            print(i, end= ", ")
        else :
            print(i, end="")
    print(".")
    if len(lista_livro_outra_saga) >= 1 :
        print(f'Cuidado, Sérgio! Você está organizando seus livros de uma forma errada, o(s) livro(s): ', end = "")
        for n in lista_livro_outra_saga :
            print(n, end= ", ")
        print('não faz(em) parte da saga "Percy Jackson e os Olimpianos".')