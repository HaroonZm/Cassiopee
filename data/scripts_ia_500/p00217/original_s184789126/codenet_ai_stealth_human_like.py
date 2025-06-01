while True:
    N = int(input())  # nombre d'éléments à lire
    if N == 0:
        break  # fin du programme si entrée zéro

    best_player = 0
    best_score = 0
    for _ in range(N):
        player, d, g = map(int, input().split())
        total = d + g
        # on cherche le score max
        if total > best_score:
            best_score = total
            best_player = player
    print(best_player, best_score)  # affichage du "meilleur" joueur et score associé