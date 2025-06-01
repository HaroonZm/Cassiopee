def obtenir_entrée():
    ligne = 0
    while True:
        try:
            entrée = input()
            if not entrée:  # Pour éviter les lignes vides indésirables
                continue
            yield ''.join(entré for entré in entrée)
            ligne += 1
        except EOFError:
            break

N = list(obtenir_entrée())
index = 0
while index < len(N):
    première_liste = list(map(lambda x: int(x), N[index].split()))
    seconde_liste = list(map(lambda x: int(x), N[index + 1].split()))

    compteur_hit = sum(1 for i, val in enumerate(première_liste) if i < len(seconde_liste) and val == seconde_liste[i])
    compteur_blow = 0
    for x in première_liste:
        if x in seconde_liste:
            if première_liste.index(x) != seconde_liste.index(x):
                compteur_blow += 1

    print(compteur_hit, compteur_blow)
    index += 2