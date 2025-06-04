# Bon, alors on fait une boucle infinie, avant de voir si la condition de sortie est ok
while True:
    # On prend 2 entiers, séparés par un espace
    n, m = map(int, raw_input().split())
    if n == 0 and m == 0:
        break  # On arrête tout si c'est 0 0

    # Je charge les listes 'up' et 'down', mais attention aux entrées nulles
    up = []
    if n != 0:
        up = map(int, raw_input().split())
    down = []
    if m != 0:
        down = map(int, raw_input().split())
    
    # On combine tout, c'est plus simple comme ça
    all_vals = up + down
    all_vals.sort()  # Je trie, normal non ?

    # J'essaie de trouver la plus grande différence consécutive
    if len(all_vals) > 0:
        current_max = all_vals[0]
        for j in range(0, len(all_vals) - 1):
            diff = all_vals[j+1] - all_vals[j]
            if diff > current_max:
                current_max = diff
        print current_max
    else:
        # hmm, dans ce cas, on affiche zéro, ça a du sens ?
        print 0