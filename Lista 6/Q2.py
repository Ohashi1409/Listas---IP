nome_escola = ''
tema_escola = ''
tempo_desfile = ''
quesitos = ''
nota_final = 0
tempo_escolas = {}
media_escolas = {}
media_nota_final = {}
escola_vencedora = {}
dict_geral = {}
dict_escolas = {}
tipos_quesitos = {}

while nome_escola != 'Não há mais escolas':
    nome_escola = input()
    if nome_escola != 'Não há mais escolas':
        tema_escola = input()
        tempo_desfile = input()
        tempo_escolas.update({nome_escola: tempo_desfile})

print('Desfile de samba do Rio de janeiro 2024')

while quesitos != 'Não há mais quesitos':
    quesitos = input()
    if quesitos != 'Não há mais quesitos':
        print(f'Vamos às notas para o quesito {quesitos}:')
        for keys in tempo_escolas.keys():
            nota_no_quesito = tuple(input().split(' - '))
            print(f'{nota_no_quesito[0]}: {nota_no_quesito[1]}')
            dict_escolas.update({nota_no_quesito[0]: nota_no_quesito[1]})
            dict_geral.update({quesitos: dict(dict_escolas)})

for quesitos, escola in dict_geral.items():
    for escola, nota in escola.items():
        if escola not in media_escolas.keys():
            media_escolas[escola] = {'total': 0, 'rep': 0}
        media_escolas[escola]['total'] += float(nota)
        media_escolas[escola]['total'] = round(media_escolas[escola]['total'], 2)
        media_escolas[escola]['rep'] += 1

media_nota_final = {escola: dado['total']/dado['rep'] for escola, dado in media_escolas.items()}

for tempos in tempo_escolas.values():
        if int(tempos) < 65:
            nota_final = round(((65-int(tempos))*0.1), 2)
            for keys in tempo_escolas.keys():
                if tempo_escolas.get(keys) == tempos:
                    media_nota_final.update({keys: round(float(float(media_nota_final.get(keys)) - nota_final), 2)})
        elif int(tempos) > 75:
            nota_final = round(((int(tempos)-75)*0.1), 2)
            for keys in tempo_escolas.keys():
                if tempo_escolas.get(keys) == tempos:
                    media_nota_final.update({keys: round(float(float(media_nota_final.get(keys)) - nota_final), 2)})

escola_vencedora = sorted(media_nota_final.items(), key = lambda x:x[1], reverse=True)   

print('E o vencedor do desfile de escola de samba do Rio de Janeiro de 2024 é:')
print(f'{escola_vencedora[0][0]} com uma nota final de {escola_vencedora[0][1]}!')