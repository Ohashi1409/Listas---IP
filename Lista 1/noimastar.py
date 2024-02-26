local_do_teste = input()
hora_do_teste = int(input())
resposta = input()
if local_do_teste == "Salão" and resposta == "Sim, Pearl! Siga seus sonhos!" :
    hora_do_teste -= 2
    print("Em direção ao salão!")
    print(f"Pra chegar na hora, vou ter que sair de {hora_do_teste} horas.")
    print("Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!")
elif local_do_teste == "Salão" and resposta == "Não. Você ficará na fazenda." :
    hora_do_teste -= 2
    print("Em direção ao salão!")
    print(f"Pra chegar na hora, vou ter que sair de {hora_do_teste} horas.")
    print("Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!")
elif local_do_teste == "Praça" and resposta == "Sim, Pearl! Siga seus sonhos!" :
    hora_do_teste -= 2
    print("Para a praça eu vou!")
    print(f"Pra chegar na hora, vou ter que sair de {hora_do_teste} horas.")
    print("Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!")
elif local_do_teste == "Praça" and resposta == "Não. Você ficará na fazenda." :
    hora_do_teste -= 2
    print("Para a praça eu vou!")
    print(f"Pra chegar na hora, vou ter que sair de {hora_do_teste} horas.")
    print("Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!")
elif local_do_teste == "Centro da cidade" and resposta == "Sim, Pearl! Siga seus sonhos!" :
    hora_do_teste -= 1
    print("Faz tempo que não visito o centro, mal posso esperar!")
    print(f"Pra chegar na hora, vou ter que sair de {hora_do_teste} horas.")
    print("Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!")
elif local_do_teste == "Centro da cidade" and resposta == "Não. Você ficará na fazenda." :
    hora_do_teste -= 1
    print("Faz tempo que não visito o centro, mal posso esperar!")
    print(f"Pra chegar na hora, vou ter que sair de {hora_do_teste} horas.")
    print("Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!")