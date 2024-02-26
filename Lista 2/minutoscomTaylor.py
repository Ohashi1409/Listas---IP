opiniao = str()
quant_min = int()
rep = 0
rep_mesma_msc = 0
while rep < 21 :
    if opiniao != "parei" :
        opiniao = input()
        if opiniao == "amei" :
            quant_min += 4
        elif opiniao == "não parei de ouvir" :
            opiniao2 = str()
            while opiniao2 != "pulei" :
                if rep_mesma_msc <= 10 :
                    opiniao2 = input()
                    rep_mesma_msc += 1
                    quant_min += 4
                else : 
                    break
            else :
                quant_min -= 4
        elif opiniao == "essa não deu" :
            quant_min += 0
        elif opiniao == "escutei só metade" :
            quant_min += 2
    else :
        print(f"Você ouviu {quant_min} minutos hoje!!!")
        break
    rep += 1
else : 
    print(f"Você ouviu {quant_min} minutos hoje!!!")