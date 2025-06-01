nombre_de_parties = int(input())
for _ in range(nombre_de_parties):
    nombre_de_outs = 0
    nombre_de_coureurs = 0
    score_total = 0
    while nombre_de_outs < 3:
        evenement = input()
        if evenement == 'HIT':
            if nombre_de_coureurs < 3:
                nombre_de_coureurs += 1
            else:
                score_total += 1
        elif evenement == 'HOMERUN':
            score_total += nombre_de_coureurs + 1
            nombre_de_coureurs = 0
        elif evenement == 'OUT':
            nombre_de_outs += 1
    print(score_total)