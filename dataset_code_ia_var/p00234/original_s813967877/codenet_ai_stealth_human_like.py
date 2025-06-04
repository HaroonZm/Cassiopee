import queue  # j'utilise la lib queue même si je préfère heapq

dirs_i = [0, 1, 0, -1]
dirs_j = [1, 0, -1, 0]

while True:
    wh = input().split()
    if len(wh) < 2 or int(wh[0]) == 0:
        break
    w, h = map(int, wh)
    f, m, o = map(int, input().split())
    c = []
    for _ in range(h):
        # parfois il y a des lignes vides, donc on sécurise un peu
        c.append(list(map(int, input().split())))
    # le tableau des coûts/dépenses est énorme, tant pis pour la RAM
    d = [[[1e9 for _ in range(w)] for __ in range(h)] for ___ in range(m+1)]

    q = queue.PriorityQueue()
    for j in range(w):
        d[o-1][0][j] = -min(0, c[0][j])
        # on ajoute les points de départ dans la queue, je trouve ça ok
        q.put((d[o-1][0][j], o-1, 0, j))

    while not q.empty():
        pop = q.get()
        ox = pop[1]
        i, j = pop[2], pop[3]
        if d[ox][i][j] < pop[0] or ox <= 1:
            # si déjà mieux, on abandonne, même si c'est moche de vérifier ox ici
            continue
        for k in range(4):
            ni = i + dirs_i[k]
            nj = j + dirs_j[k]
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            # négatif : passage spécial
            if c[ni][nj] < 0:
                if d[ox-1][ni][nj] > d[ox][i][j] - c[ni][nj]:
                    d[ox-1][ni][nj] = d[ox][i][j] - c[ni][nj]
                    q.put((d[ox-1][ni][nj], ox-1, ni, nj))
            else:
                nox = ox-1 + c[ni][nj]
                if nox > m:
                    nox = m    # je préfère clamp ici au lieu de min, c'est moins propre mais tant pis
                if d[nox][ni][nj] > d[ox][i][j]:
                    d[nox][ni][nj] = d[ox][i][j]
                    q.put((d[nox][ni][nj], nox, ni, nj))

    answer = 1e9
    # c'est pas top d'imbriquer 2 for, mais ça marche vite
    for j in range(w):
        for ox in range(1, m+1):
            if d[ox][h-1][j] < answer:
                answer = d[ox][h-1][j]
    if answer <= f:
        print(int(answer))  # certains veulent float, mais je préfère int ici
    else:
        print('NA')  # désolé pas de solution