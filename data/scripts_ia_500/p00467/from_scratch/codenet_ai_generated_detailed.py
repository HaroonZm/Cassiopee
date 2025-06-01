while True:
    # Lecture des valeurs N et M
    N, M = map(int, input().split())
    # Condition d'arrêt
    if N == 0 and M == 0:
        break

    # Lecture des instructions pour chaque case du plateau
    instructions = [int(input()) for _ in range(N)]

    # Lecture des résultats des lancers de dés
    dice = [int(input()) for _ in range(M)]

    position = 0  # Position initiale (index 0 correspond à la case 1)
    moves = 0     # Nombre de lancers effectués

    for roll in dice:
        moves += 1
        position += roll  # Avancer selon le lancer de dé

        # Si on dépasse ou atteint la dernière case, on a gagné
        if position >= N - 1:
            print(moves)
            break

        # Appliquer l'instruction sur la case atteinte
        position += instructions[position]

        # Vérifier à nouveau si on a atteint ou dépassé la dernière case
        if position >= N - 1:
            print(moves)
            break