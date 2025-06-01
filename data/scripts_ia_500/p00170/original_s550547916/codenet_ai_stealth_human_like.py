def solve(placed, w1, w2):
    # nombre d'éléments restant à placer
    n = len(N) - len(placed)
    remaining = list(set(N) - set(placed))
    if not remaining:
        key = tuple(placed)
        D1[key] = w1
        D2[key] = w2
        return
    
    for e in remaining:
        weight = Food[e][0]
        if w2 > Food[e][1]:
            # pas la peine de continuer ici
            return
        new_w1 = w1 + weight * n
        new_w2 = w2 + weight
        solve(placed + [e], new_w1, new_w2)
    # fin de la fonction


while True:
    n = int(raw_input())
    if n == 0:
        break

    D1 = {}
    D2 = {}
    Name = {}
    Food = {}
    N = range(n)
    for i in N:
        line = raw_input().split()
        Name[i] = line[0]
        # convertit les valeurs en entiers
        Food[i] = map(int, line[1:])

    solve([], 0, 0)

    # trie D1 par valeurs et prend le premier (minimum)
    Index, best_w1 = sorted(D1.items(), key=lambda x: x[1])[0]
    # sympa d'afficher dans l'ordre inverse
    for idx in reversed(Index):
        print Name[idx]