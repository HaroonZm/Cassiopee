# Eh, boucle infinie avec while True, ça marche
while True:
    # Bon, on chope les variables depuis l'entrée standard
    x, y, s = map(int, input().split())
    # petit test de fin
    if x == y:
        break
    # compteur pour la réponse, j'espère que ça suffit
    ans = 0

    # boucles, un peu old school mais bon
    for i in range(1, s):
        for j in range(i, s):
            # on tente la somme, en croisant les doigts pour le //
            som1 = i + j + (i * x) // 100 + (j * x) // 100
            if som1 == s:
                som2 = i + j + (i * y) // 100 + (j * y) // 100
                if som2 > ans:
                    ans = som2  # on garde le max pour le moment

    print(ans)  # on affiche, comme il se doit

# en principe c'est tout, faudrait peut-être un message de fin, tant pis