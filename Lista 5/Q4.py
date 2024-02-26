def bin_to_dec(lista_binarios):
    result=0
    if len(lista_binarios) == 0:
        return result
    else:
        result = int(lista_binarios[0])*(2**(len(lista_binarios)-1))
        result += bin_to_dec(lista_binarios[1:])

    return result

def dec_to_string(lista_binarios):
    info_final = ''

    if len(lista_binarios) == 0:
        return info_final
    else:
        info_final += chr(bin_to_dec(lista_binarios[0]))
        info_final += dec_to_string(lista_binarios[1:])

    return info_final

lista_binarios = input().split(' ')
print(f'Os códigos da Matrix indicam que {dec_to_string(lista_binarios)} está perto.')