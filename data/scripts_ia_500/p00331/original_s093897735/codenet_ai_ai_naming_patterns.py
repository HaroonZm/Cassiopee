hauteur, resultat = map(int, input().split())
if hauteur < 0:
    somme_hauteur_resultat = hauteur + resultat
    if somme_hauteur_resultat < 0:
        print(-1)
    elif somme_hauteur_resultat == 0:
        print(0)
    else:
        print(1)
else:
    print(1)