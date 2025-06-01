while True:
    N, K = map(int, input().split())
    if N == 0:
        # fin du programme
        break
    S = [0]  # j'ajoute un 0 au début pour que les indices matchent
    S += list(map(int, input().split()))
    possible = True  # je change un peu le nom de la variable
    
    for _ in range(N):
        usage = list(map(int, input().split()))
        for idx, val in enumerate(usage):
            S[idx+1] -= val
            if S[idx+1] < 0:
                possible = False
                break  # on sort direct car c'est perdu
        if not possible:
            break  # pas la peine de continuer si ça foire déjà
    
    if possible:
        print("Yes")
    else:
        print("No")