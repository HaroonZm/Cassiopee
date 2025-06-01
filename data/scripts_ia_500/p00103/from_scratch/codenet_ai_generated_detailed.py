n = int(input())  # Nombre de datasets

for _ in range(n):
    outs = 0         # Nombre de sorties dans l'inning
    score = 0        # Score courant dans l'inning
    # La base [first, second, third] : True si occupée, False sinon
    bases = [False, False, False]

    while outs < 3:
        event = input().strip()
        if event == "HIT":
            # Avancer les coureurs sur les bases : de la 3e vers la maison, puis 2e vers 3e, 1ère vers 2e
            # Le coureur en 3e base marque un point
            if bases[2]:
                score += 1
            # Avance les coureurs
            bases[2] = bases[1]
            bases[1] = bases[0]
            bases[0] = True  # Nouvelle arrivée en 1ère base

        elif event == "HOMERUN":
            # Tous les coureurs et le batteur marquent
            runners = sum(bases)
            score += runners + 1
            # Bases vidées
            bases = [False, False, False]

        elif event == "OUT":
            outs += 1
        else:
            # Si une entrée inconnue est donnée, on sort de la boucle pour éviter blocage
            break

    print(score)