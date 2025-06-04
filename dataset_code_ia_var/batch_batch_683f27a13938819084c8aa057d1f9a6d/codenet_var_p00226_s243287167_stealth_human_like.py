# Bon, alors voilà le code réécrit un peu à ma sauce...

while True:
    a, b = raw_input().split()  # raw_input pour Python 2 (old school!)
    if a == "0":
        break  # Hop, on arrête tout si c'est zéro
    hits = 0
    blows = 0
    # boucle sur 4... c'est censé être 4 chiffres
    for j in range(4):
        if a[j] == b[j]:
            hits += 1  # bien placé
        elif a[j] in b:
            blows += 1  # mal placé mais présent (ça prend pas en compte les doublons...)
    print hits, blows  # bon, affichage classique

# à revoir si tu veux gérer les doublons différemment, mais ça marche pour l'instant