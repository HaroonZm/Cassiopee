while True:
    X, Y, n = map(int, input().split())
    if X == 0 and Y == 0 and n == 0:
        break
    buyers = []
    for _ in range(n):
        b, k = map(int, input().split())
        buyers.append((b, k))
    s = []
    for _ in range(Y):
        row = list(map(int, input().split()))
        s.append(row)

    # On compte le nombre de cases pour chaque acheteur dans le grille
    count_s = {}
    for y in range(Y):
        for x in range(X):
            if s[y][x] != 0:
                count_s[s[y][x]] = count_s.get(s[y][x], 0) + 1

    # Vérifie que les clés et comptes correspondent
    if len(count_s) != n:
        print("NA")
        continue
    ok = True
    for b,k in buyers:
        if count_s.get(b,0) != k:
            ok = False
            break
    if not ok:
        print("NA")
        continue

    # Recherche les rectangles possibles pour chaque acheteur
    # stocke toutes les possibilités par acheteur
    candidates = {}
    for b,k in buyers:
        candidates[b] = []
        # parcours toutes les rectangles possibles
        for top in range(Y):
            for left in range(X):
                for bottom in range(top, Y):
                    for right in range(left, X):
                        w = right - left + 1
                        h = bottom - top + 1
                        if w*h != k:
                            continue
                        # Vérifie que toutes les cases dans le rectangle sont b ou zero
                        ok_rect = True
                        actual_count = 0
                        for yy in range(top, bottom+1):
                            for xx in range(left, right+1):
                                if s[yy][xx] != 0 and s[yy][xx] != b:
                                    ok_rect = False
                                    break
                                if s[yy][xx] == b:
                                    actual_count += 1
                            if not ok_rect:
                                break
                        if not ok_rect:
                            continue
                        if actual_count == k:
                            candidates[b].append((top,left,bottom,right))

    # Il faut maintenant vérifier s'il y a exactement une façon de découper le terrain.
    # On fera un backtracking sur les acheteurs, en assignant un rectangle à chacun,
    # vérifiant qu'ils ne se chevauchent pas et couvrent toutes les cases.
    ans = None
    used = [[False]*X for _ in range(Y)]

    def can_place(rect):
        top,left,bottom,right = rect
        for yy in range(top,bottom+1):
            for xx in range(left,right+1):
                if used[yy][xx]:
                    return False
        return True

    def place(rect,val):
        top,left,bottom,right = rect
        for yy in range(top,bottom+1):
            for xx in range(left,right+1):
                used[yy][xx] = val

    # Pour recontruire la solution, on stocke l'affectation
    assign = {}

    all_bs = [b for b,_ in buyers]

    solved = 0
    unique_solution = True

    def dfs(i):
        nonlocal ans, solved, unique_solution
        if i == len(all_bs):
            solved += 1
            if solved == 1:
                # construire la grille resultat
                res = [[0]*X for _ in range(Y)]
                for b in assign:
                    top,left,bottom,right = assign[b]
                    for yy in range(top,bottom+1):
                        for xx in range(left,right+1):
                            res[yy][xx] = b
                ans = res
            elif solved > 1:
                unique_solution = False
            return
        b = all_bs[i]
        for rect in candidates[b]:
            if can_place(rect):
                place(rect,True)
                assign[b] = rect
                dfs(i+1)
                if solved > 1:
                    return
                place(rect,False)
                del assign[b]

    dfs(0)

    if solved != 1 or not unique_solution:
        print("NA")
    else:
        for row in ans:
            print(" ".join(str(x) for x in row))