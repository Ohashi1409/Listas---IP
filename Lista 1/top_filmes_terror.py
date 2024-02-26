filme1 = input()
pontuacao_global_1 = float(input())
critica1 = input()
if critica1 == "boa" :
    pontuacao_global_1 = float(pontuacao_global_1*5/4)
elif critica1 == "media" :
    pontuacao_global_1 = float(pontuacao_global_1*1)
elif critica1 == "ruim" :
    pontuacao_global_1 = float(pontuacao_global_1*3/4)
elif critica1 == "pessima" :
    pontuacao_global_1 = 0

filme2 = input()
pontuacao_global_2 = float(input())
critica2 = input()
if critica2 == "boa" :
    pontuacao_global_2 = float(pontuacao_global_2*5/4)
elif critica2 == "media" :
    pontuacao_global_2 = float(pontuacao_global_2*1)
elif critica2 == "ruim" :
    pontuacao_global_2 = float(pontuacao_global_2*3/4)
elif critica2 == "pessima" :
    pontuacao_global_2 = 0

filme3 = input()
pontuacao_global_3 = float(input())
critica3 = input()
if critica3 == "boa" :
    pontuacao_global_3 = float(pontuacao_global_3*5/4)
elif critica3 == "media" :
    pontuacao_global_3 = float(pontuacao_global_3*1)
elif critica3 == "ruim" :
    pontuacao_global_3 = float(pontuacao_global_3*3/4)
elif critica3 == "pessima" :
    pontuacao_global_3 = 0

if (pontuacao_global_1 > pontuacao_global_2) and (pontuacao_global_1 > pontuacao_global_3):
    if pontuacao_global_2 > pontuacao_global_3 :
        if critica3 == "pessima" :
            print("**** TOP 3 FILMES ****")
            print(f"{filme1} está em 1° lugar") 
            print(f"{filme2} está em 2° lugar")
            print(f"{filme3} está em 3° lugar")
            print(f"{filme3} teve uma crítica péssima")
        else : 
            print("**** TOP 3 FILMES ****")
            print(f"{filme1} está em 1° lugar")
            print(f"{filme2} está em 2° lugar")
            print(f"{filme3} está em 3° lugar")
    else : 
        if critica2 == "pessima" :
            print("**** TOP 3 FILMES ****")
            print(f"{filme1} está em 1° lugar") 
            print(f"{filme3} está em 2° lugar")
            print(f"{filme2} está em 3° lugar")
            print(f"{filme2} teve uma crítica péssima")
        else : 
            print("**** TOP 3 FILMES ****")
            print(f"{filme1} está em 1° lugar")
            print(f"{filme3} está em 2° lugar")
            print(f"{filme2} está em 3° lugar")
else :
    if (pontuacao_global_2 > pontuacao_global_1) and (pontuacao_global_2 > pontuacao_global_3) :
        if pontuacao_global_1 > pontuacao_global_3 :
            if critica3 == "pessima" :
                print("**** TOP 3 FILMES ****")
                print(f"{filme2} está em 1° lugar") 
                print(f"{filme1} está em 2° lugar")
                print(f"{filme3} está em 3° lugar")
                print(f"{filme3} teve uma crítica péssima")
            else :
                print("**** TOP 3 FILMES ****")
                print(f"{filme2} está em 1° lugar")
                print(f"{filme1} está em 2° lugar")
                print(f"{filme3} está em 3° lugar")
        else : 
            if critica1 == "pessima" :
                print("**** TOP 3 FILMES ****")
                print(f"{filme2} está em 1° lugar") 
                print(f"{filme3} está em 2° lugar")
                print(f"{filme1} está em 3° lugar")
                print(f"{filme1} teve uma crítica péssima")
            else :
                print("**** TOP 3 FILMES ****")
                print(f"{filme2} está em 1° lugar")
                print(f"{filme3} está em 2° lugar")
                print(f"{filme1} está em 3° lugar")
    else :
        if (pontuacao_global_3 > pontuacao_global_1) and (pontuacao_global_3 > pontuacao_global_2) :
            if pontuacao_global_1 > pontuacao_global_2 :
                if critica2 == "pessima" :
                    print("**** TOP 3 FILMES ****")
                    print(f"{filme3} está em 1° lugar") 
                    print(f"{filme1} está em 2° lugar")
                    print(f"{filme2} está em 3° lugar")
                    print(f"{filme2} teve uma crítica péssima")
                else : 
                    print("**** TOP 3 FILMES ****")
                    print(f"{filme3} está em 1° lugar")
                    print(f"{filme1} está em 2° lugar")
                    print(f"{filme2} está em 3° lugar")
            else : 
                if critica1 == "pessima" :
                    print("**** TOP 3 FILMES ****")
                    print(f"{filme3} está em 1° lugar") 
                    print(f"{filme2} está em 2° lugar")
                    print(f"{filme1} está em 3° lugar")
                    print(f"{filme1} teve uma crítica péssima")
                else :
                    print("**** TOP 3 FILMES ****")
                    print(f"{filme3} está em 1° lugar")
                    print(f"{filme2} está em 2° lugar")
                    print(f"{filme1} está em 3° lugar")