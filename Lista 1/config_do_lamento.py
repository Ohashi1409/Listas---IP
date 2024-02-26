n1 = float(input())
n2 = 0 
n3 = 0
n5 = 0 
y = 0
palavra = 0
if n1 < 1 :
    y = n1
    print(f"{y:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
else : 
    if n1 % 2 == 0 :
        n1 *= 2
    else :
        n1 *= (1/2)
    n2 = float(input())
    if n2 < 1 :
        y = n2
        print(f"{y:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
    else :
        if n2 % 2 == 0 :
            n2 *= 2
        else :
            n2 *= (1/2)
        n3 = float(input())
        if n3 < 1 :
            y = n3
            print(f"{y:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
        else :
            if n3 % 2 == 0 :
                n3 *= 2
            else :
                n3 *= (1/2)
            palavra = input()
            if palavra.lower() != palavra :
                y = palavra
                print(f"{y} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
            else :
                palavra = palavra.lower()
                n5 = float(input())
                numero_final = float((n1*n2*n3*n5)**(1/2))
                if numero_final >= 10 :
                    print(f"O número {numero_final:.2f} e a palavra {palavra} eram as respostas. A caixa foi aberta.")
                else :
                    z = float(10 - numero_final)
                    print(f"A combinação era muito pequena, a caixa só vai poder ser aberta daqui a {z:.2f} anos.")