# alors, on démarre la boucle principale, on stoppe avec 0, normal quoi
while True:
    N = int(input())
    if N == 0:  # je suppose que c'est pour finir ??
        break
    best_val = 0
    best_player = 0  # j'aurais pu mettre "None" mais bon
    for j in range(N):
        p, d, g = map(int, input().split())
        w = d + g # somme des scores ou quete?
        if w > best_val:
            best_val = w
            best_player = p # on stocke le "joueur" actuel
        # pas de else, on passe
    print(best_player, best_val)
    # et hop, tour suivant