lugar_show = input()
codigo_vip = str()
pessoas_com_vip = 0
while (codigo_vip != "0000") :
    codigo_vip = input()
    if codigo_vip == "1000" :
        print("Mais um VIP! Não podemos esquecer de contabilizá-lo.")
        pessoas_com_vip += 1
    elif codigo_vip == "1001" :
        print("Ingresso Normal. Não iremos contabilizá-lo.")
    elif codigo_vip == "1002" :
        print("Ele ficará na frente do show, porém não é VIP! Não será contabilizado também.")
    elif codigo_vip == "1003" :
        print("Espera, quem é esse? Ele não pagou! Não devemos sequer analisar sua entrada.")
    elif codigo_vip == "1004" :
        print("Esse código não existe! O sistema quebrou...")
        print("Vamos aguardar até que o suporte nos ajude.")
        suporte = 0
        while suporte != "Ajudou" :
            suporte = input()
            if suporte != "Ajudou" :
                print("Ainda não...")
        else :
            print(f"O show da Taylor Swift será em {lugar_show} e contará com {pessoas_com_vip} VIPs!")
            break
else :
    print(f"O show da Taylor Swift será em {lugar_show} e contará com {pessoas_com_vip} VIPs!")