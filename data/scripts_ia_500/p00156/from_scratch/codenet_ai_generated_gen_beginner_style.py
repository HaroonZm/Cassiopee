from collections import deque

while True:
    line = input().strip()
    if line == '0 0':
        break
    n, m = map(int, line.split())
    grid = [input() for _ in range(m)]

    # Trouver la position du chateau '&'
    castle = None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '&':
                castle = (i, j)
                break
        if castle:
            break

    # Positions extérieures: les bords non murailles
    starts = []
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                if grid[i][j] != '#':
                    starts.append((i, j))

    # BFS depuis toutes les positions extérieures
    # On garde dist[i][j] = nb minimum de sorties de la mare (quand on entre dans '#', on compte)
    from collections import deque
    INF = 10**9
    dist = [[INF]*n for _ in range(m)]
    q = deque()

    for si,sj in starts:
        dist[si][sj] = 0
        q.append((si,sj))

    while q:
        i,j = q.popleft()
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < m and 0 <= nj < n:
                cost = dist[i][j]
                # Si on bouge d'un '.' ou '&' vers un '#', on ajoute 1 au coût (on entre dans un fossé)
                if grid[ni][nj] == '#':
                    # On est entrain d'entrer dans le fossé, on compte +1
                    if dist[ni][nj] > cost + 1:
                        dist[ni][nj] = cost + 1
                        q.append((ni,nj))
                else:
                    # '.' ou '&'
                    if dist[ni][nj] > cost:
                        dist[ni][nj] = cost
                        q.appendleft((ni,nj))  # Mettre devant la file car pas d'augmentation du coût

    # Le nombre minimal d'entrees dans le fossé est dist[castle]
    # Mais on cherche combien de fois il faut "se hisser hors du fossé"
    # Or entrer dans le fossé est compté,
    # Chaque entrée dans le fossé correspond à une fois où il faut se hisser hors.
    # Donc on doit compter combien de fois on sort du fossé. 
    # Ici, le coût compte les entrées dans fossé.
    # Puisque on commence hors du fossé, ce nombre correspond bien au nombre de remontées.
    print(dist[castle[0]][castle[1]])