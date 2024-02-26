zeus = ["Zeus", "trovão", "deus"]
afrodite = ["Afrodite", "amor", "deusa"]
poseidon = ["Poseidon", "oceanos", "deus"]
hercules = ["Hércules", "força", "semideus"]
aquiles = ["Aquiles", "resistência", "semideus"]
orfeu = ["Orfeu", "música", "semideus"]
num_questao = 1
qtd_acertos = 0
qtd_questoes = int(input())

if qtd_questoes == 0 :
    print("Infelizmente, Percy Jackson, chegou atrasado para a exame...")
else :
    for i in range(1, qtd_questoes+1) :
        acertos = 0
        resp_percy = input().split(", ")

        if "Zeus" in resp_percy :
            if "trovão" in resp_percy :
                if "deus" in resp_percy :
                    print(f"A resposta da {num_questao}ª questão está... CORRETA!")
                    qtd_acertos += 1
                else : 
                    print(f"A resposta da {num_questao}ª questão está... ERRADA!")
            else :
                print(f"A resposta da {num_questao}ª questão está... ERRADA!")
        elif "Afrodite" in resp_percy :
            if "amor" in resp_percy :
                if "deusa" in resp_percy :
                    print(f"A resposta da {num_questao}ª questão está... CORRETA!")
                    qtd_acertos += 1
                else : 
                    print(f"A resposta da {num_questao}ª questão está... ERRADA!")
            else :
                print(f"A resposta da {num_questao}ª questão está... ERRADA!")
        elif "Poseidon" in resp_percy :
            if "oceanos" in resp_percy :
                if "deus" in resp_percy :
                    print(f"A resposta da {num_questao}ª questão está... CORRETA!")
                    qtd_acertos += 1
                else : 
                    print(f"A resposta da {num_questao}ª questão está... ERRADA!")
            else :
                print(f"A resposta da {num_questao}ª questão está... ERRADA!")
        elif "Hércules" in resp_percy :
            if "força" in resp_percy :
                if "semideus" in resp_percy :
                    print(f"A resposta da {num_questao}ª questão está... CORRETA!")
                    qtd_acertos += 1
                else : 
                    print(f"A resposta da {num_questao}ª questão está... ERRADA!")
            else :
                print(f"A resposta da {num_questao}ª questão está... ERRADA!")
        elif "Aquiles" in resp_percy :
            if "resistência" in resp_percy :
                if "semideus" in resp_percy :
                    print(f"A resposta da {num_questao}ª questão está... CORRETA!")
                    qtd_acertos += 1
                else : 
                    print(f"A resposta da {num_questao}ª questão está... ERRADA!")
            else :
                print(f"A resposta da {num_questao}ª questão está... ERRADA!")
        elif "Orfeu" in resp_percy :
            if "música" in resp_percy :
                if "semideus" in resp_percy :
                    print(f"A resposta da {num_questao}ª questão está... CORRETA!")
                    qtd_acertos += 1
                else : 
                    print(f"A resposta da {num_questao}ª questão está... ERRADA!")
            else :
                print(f"A resposta da {num_questao}ª questão está... ERRADA!")
        else :
            print(f"A resposta da {num_questao}ª questão está... ERRADA!")

        i += 1
        num_questao += 1

    porcentagem = int(((qtd_acertos/qtd_questoes)*100))
    print(f"Percy Jackson, sua taxa de acerto no EDEM é de aproximadamente... {porcentagem}%")
    if porcentagem == 100 :
        print("UAU, você gabaritou! Você é praticamente um deus do Olimpo!")
    elif 60 <= porcentagem < 100 :
        print("Muito bem, você quase pode começar a desfilar entre os semideuses!")
    elif 20 <= porcentagem < 60 :
        print("Você pode melhorar um pouco mais!")
    else : 
        print("Bem... te vejo ano que vem")