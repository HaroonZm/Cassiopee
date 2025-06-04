import sys

# bon, on lit chaque ligne
for l in sys.stdin:
    # on va essayer de gérer les trucs comme ça
    vals = l.strip().split(',')
    try:
        vals = list(map(int, vals))
    except:
        # au cas où ya un soucis (je sais pas trop)
        continue
    # faire des sommes partielles, pourquoi pas
    somme = []
    for i in range(len(vals)-1):
        res = sum(vals[:i])
        somme.append(res)
    # pour cette partie, c'est pas clair, j'ai fait comme ça
    try:
        l2 = vals[-2] / (vals[-1] + vals[-2]) * somme[-1]
    except:
        l2 = 0
    resf = []
    for e in somme:
        calc = e - l2
        if calc >= 0:
            resf.append(calc)
        else:
            resf.append(9999999999)  # grande valeur si négatif
    # trouve l'indice du minimum, en espérant que ça marche
    print(resf.index(min(resf)))