palavra_grega = input()
mensagem_grega = []
mensagem_decifrada = []
algarismos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
erro = False

for i in palavra_grega :
    mensagem_grega.append(ord(i))

for n in mensagem_grega :
    if n == 32 :
        mensagem_decifrada.append(' ')
    else :
        mensagem_decifrada.append(chr(n + len(mensagem_grega)))

for numeros in algarismos :
    if numeros in mensagem_decifrada :
        erro = True

if (len(mensagem_decifrada) == 0) or (mensagem_grega[0]==32):
    print("Ué não tem nada para me decifrar aqui")
elif erro :
    print("Algo de errado não está certo. Será que estou ficando doido?")
else : 
    print("Descobri o que a mensagem significa: ", end= "")
    for letras in mensagem_decifrada :
        print(letras, end="")