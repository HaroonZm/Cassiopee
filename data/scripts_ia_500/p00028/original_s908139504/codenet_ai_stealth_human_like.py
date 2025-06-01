dico = {}
while True:
    try:
        n = int(raw_input())  # je lis un entier ici
        if n not in dico:
            dico[n] = 1
        else:
            dico[n] += 1  # incrémentation
    except EOFError:
        # trouver le(s) nombre(s) le(s) plus fréquent(s)
        max_freq = 0
        count = 0
        for key, val in sorted(dico.items(), key=lambda item: item[1], reverse=True):
            if count == 0:
                max_freq = val
            if val != max_freq:
                break
            print key  # affichage des clés principales
            count += 1
        break