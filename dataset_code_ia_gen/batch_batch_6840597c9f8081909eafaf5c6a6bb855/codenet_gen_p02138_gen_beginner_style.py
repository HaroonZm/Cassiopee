N, M = map(int, input().split())

# HP de chaque joueur est 2 initialement
# chaque tour, une équipe attaque exactement une fois par joueur,
# baisse le HP d'autant d'adversaires, éliminant ceux dont HP atteint 0.
# Le score augmente de 1 à chaque fois que tous les joueurs d'une équipe ont attaqué sans que l'autre soit éliminé.

# On simule simplement en suivant les règles, mais comme N et M peuvent être très grands,
# simuler joueur par joueur est impossible.
# On implémente une simulation simple en suivant le principe, ce que ferait un débutant:

uku = [2] * N
ushi = [2] * M

score = 0
uku_turn = True  # True si c'est le tour de UKU d'attaquer, False sinon

while True:
    if uku_turn:
        # UKU attaque ushi
        attacks = len(uku)
        # On attaque les premiers joueurs vivants de ushi
        for i in range(len(ushi)):
            if attacks == 0:
                break
            if ushi[i] > 0:
                ushi[i] -= 1
                if ushi[i] == 0:
                    # éliminer
                    pass
                attacks -= 1
        # Retirer les joueurs éliminés
        ushi = [h for h in ushi if h > 0]
        if len(ushi) == 0:
            break
        else:
            score += 1
            uku_turn = False
    else:
        # Ushi attaque UKU
        attacks = len(ushi)
        for i in range(len(uku)):
            if attacks == 0:
                break
            if uku[i] > 0:
                uku[i] -= 1
                if uku[i] == 0:
                    pass
                attacks -= 1
        uku = [h for h in uku if h > 0]
        if len(uku) == 0:
            break
        else:
            score += 1
            uku_turn = True

print(score)