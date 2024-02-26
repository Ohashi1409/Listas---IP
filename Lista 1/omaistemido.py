frase1 = input()
carac = input()
lobisomen = ("Parou filhotada, assim vocês vão deixar todo mundo maluco.")
carac_lobis = ("Uivar")
carac_lobis2 = ("Pelos")
carac_lobis3 = ("Caninos")
frankenstein = ("Veio de novo pelo correio, deixa de ser pão duro.")
carac_frank = ("Desmontável")
carac_frank2 = ("Parafusos")
carac_frank3 = ("Morto-vivo")
homem_invisivel = ("Quem me beliscou?")
carac_homi_invisi = ("Transparente")
mumia = ("Tô na área galera!")
carac_mumia = ("Enfaixado")
carac_mumia2 = ("Morto-vivo")
if frase1 == lobisomen and (carac == carac_lobis or carac == carac_lobis2 or carac == carac_lobis3) :
    print("Bem-vindos ao Hotel Transilvânia!")
    print("Wayne, seu cachorrão.")
elif frase1 == frankenstein and (carac == carac_frank or carac == carac_frank2 or carac == carac_frank3) :
    print("Bem-vindos ao Hotel Transilvânia!")
    print("Frank, assim vai acabar perdendo a cabeça.")
elif frase1 == homem_invisivel and carac == carac_homi_invisi :
    print("Bem-vindos ao Hotel Transilvânia!")
    print("Griffin, prazer em vê-lo.")
elif frase1 == mumia and (carac == carac_mumia or carac == carac_mumia2) :
    print("Bem-vindos ao Hotel Transilvânia!")
    print("Murray, sempre soltando areia.")
elif frase1 != (lobisomen or frankenstein or homem_invisivel or mumia) or carac != (carac_lobis or carac_frank or carac_homi_invisi or carac_mumia) :
    print("UM HUMANO! Quem é você, e como você achou esse lugar?")