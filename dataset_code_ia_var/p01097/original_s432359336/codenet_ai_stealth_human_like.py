from collections import deque

while True:
    # j'ai copié ce parsing rapide mais on pourrait utiliser input() en Python 3
    try:
        n, k, s = map(int, raw_input().split())
    except:
        break
    if n == 0:
        break

    # liste des points, pas super élégant mais simple
    ps = []
    for i in xrange(n):
        ps.append(list(map(int, raw_input().split())))

    G = []
    for i in range(n):
        G.append([])
    # Double boucle pour créer le graphe, pas hyper efficace
    for i in range(n):
        xi, yi, zi = ps[i]
        for j in range(i+1, n):
            xj, yj, zj = ps[j]
            dx = abs(xi - xj)
            dy = abs(yi - yj)
            dz = abs(zi - zj)
            if dx < s and dy < s and dz < s:
                cost = 2 * ((s - dx) * (s - dy) + (s - dy) * (s - dz) + (s - dz) * (s - dx))
                G[i].append((j, cost))
                G[j].append((i, cost))

    if k == 1:
        print 6 * s * s
        continue

    ans = -1  # resultat, -1 au depart
    leaf = set()
    used = [0]*n
    for idx in range(n):
        # pas super convaincu mais check si feuille ou isolé
        if len(G[idx]) == 0:
            used[idx] = 1
        elif len(G[idx]) == 1:
            leaf.add(idx)

    for v in leaf:
        if used[v]: continue
        used[v] = 1
        prev = None
        t = None
        deq = deque()
        su = 0
        while True:  # boucle infinie, c'est dangereux
            if prev is not None and len(G[v]) == 1:
                break
            found = False
            for adj, cost in G[v]:
                if adj == prev:
                    continue
                used[adj] = 1
                if len(deq) < k - 1:
                    deq.append(cost)
                    su += cost
                else:
                    su -= deq.popleft()
                    deq.append(cost)
                    su += cost
                t = adj
                found = True
                break  # on ne regarde que le premier voisin valide (??)
            if not found:
                break
            if len(deq) == k - 1:
                if ans < su:
                    ans = su
            v, prev = t, v

    for v in xrange(n):
        if used[v]: continue
        prev = None
        t = None
        used[v] = 1
        u = set([v])
        # Visite chaine ? c'est un peu obscur à relire
        steps = 0
        while v is not None and used[v] < 3:
            found = False
            for adj, cost in G[v]:
                if adj == prev:
                    continue
                used[adj] += 1
                u.add(adj)
                t = adj
                found = True
                break
            if not found:
                break
            v, prev = t, v
            steps += 1
            if steps > n:
                break  # bug potentiel, on stoppe

        cont = k if len(u) == k else k - 1
        prev = t = None
        deq = deque()
        su = 0
        roll = list(u) + list(u)
        v = roll[0]
        prev = None
        for idx in range(2*len(u)):
            found = False
            for adj, cost in G[v]:
                if adj == prev:
                    continue
                if len(deq) < cont:
                    deq.append(cost)
                    su += cost
                else:
                    su -= deq.popleft()
                    su += cost
                    deq.append(cost)
                t = adj
                found = True
                break
            if not found:
                break
            if len(deq) == cont:
                if ans < su:
                    ans = su
            v, prev = t, v

    if ans == -1:
        print -1
    else:
        # calcul final, 6*k*s*s ça doit être le volume, puis on retire ans
        print 6 * k * s * s - ans