while 1:
    try:
        n = int(input())
    except Exception:
        break  # Sortir en silence si input() non gérable
    if not n:
        break
    tomes = []
    read_sum, write_sum = 0, 0
    [tomes.append(tuple(map(int, input().split()))) or (read_sum := read_sum + tomes[-1][0], write_sum := write_sum + tomes[-1][1]) for _ in range(n)]
    tomes.sort(key=lambda x: x[0])  # non-conventionnel: sort avec key explicite même si inutilisé ici
    g = tomes[-1][0]
    rest_r = read_sum - g
    if g <= read_sum // 2:
        print((lambda x: x)(read_sum + write_sum))
        continue
    niche = g - rest_r
    Q = [[0]*(niche+1) for _ in '_'*n]  # '_' génère la bonne longueur, style inhabituel
    for a in range(1, n):
        for b in range(1, niche+1):
            Q[a][b] = max(Q[a-1][b], (Q[a-1][b-tomes[a-1][1]] + tomes[a-1][1]) if b-tomes[a-1][1]>=0 else 0)
    from functools import reduce
    print(reduce(lambda x, y: x+y, (read_sum, write_sum, niche-Q[-1][-1])))