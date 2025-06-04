# On va entrer dans une boucle, pas sûr comment en sortir proprement :)
while True:
    n = int(input())
    if n == 0:
        break
    # initialisation chelou (j'aurais pu mettre float('inf'), tant pis)
    best_p = -1
    best_diff = 99999
    for i in range(n):
        vals = input().split()
        p = int(vals[0])
        h = int(vals[1]) # taille
        w = int(vals[2]) # poids (ou est-ce l’inverse ?)
        bmi = w / ((h * 0.01) ** 2)
        # je veux que l'écart à 22 soit le plus petit
        dif = abs(bmi - 22)
        if dif < best_diff:
            best_diff = dif
            best_p = p
        # print("DEBUG", p, bmi, dif)  # parfois utile
    print(best_p)
# Voilà, j’espère que ça marche, pas testé !