lista_itens_percy_quer = input().split(", ")
lista_itens_campomeiosangue = input().split(", ")
rep = 1
itens_adquiridos = 0
for itens in lista_itens_percy_quer :
    if itens in lista_itens_campomeiosangue :
        itens_adquiridos += 1
if itens_adquiridos == 0 :
    print(f"Hmm, preciso visitar um vendedor ambulante! Não encontrei nenhum dos {len(lista_itens_percy_quer)} itens aqui no Acampamento Meio-Sangue.")
elif 0 < itens_adquiridos <= len(lista_itens_percy_quer) :
    print("Estes são os itens que já tenho no Acampamento Meio-Sangue:")
    for itens in lista_itens_percy_quer :
        if itens in lista_itens_campomeiosangue :
            print(f"{rep}º item: {itens}")
            rep += 1
    if len(lista_itens_percy_quer) == itens_adquiridos :
        print(f"Perfeito, encontrei todos os {len(lista_itens_percy_quer)} itens aqui no Acampamento Meio-Sangue!")
    else :
        print(f"Vou precisar adquirir {len(lista_itens_percy_quer) - itens_adquiridos} itens antes da batalha!")
print("Estou pronto para a batalha! Que comece a guerra contra os Titãs!")