# Voilà mon humble version, un peu artisanale et pas parfaite mais ça tourne ;)

inf = 0x10101010
def solve(A, start):
    # On essaye de faire mieux mais c'est pas fou
    N = len(A)
    cost = [inf] * N
    seen = [0]*N
    cost[start] = 0
    while True:
        mn = inf
        nxt = -1
        seen[start] = 1
        for j in range(N):
            if seen[j]:
                continue
            if A[start][j]:
                d2 = cost[start] + A[start][j]
                if d2 < cost[j]:
                    cost[j] = d2
            if cost[j] < mn:
                mn = cost[j]
                nxt = j
        start = nxt
        if nxt == -1:
            break
    return cost


while True:
    try:
        n_m = raw_input().strip()
        if not n_m:
            continue
        n, m = map(int, n_m.split())
    except:
        break
    if n == 0:
        break
    # apparemment il vaut mieux initialiser 2 matrices...
    T = []
    C = []
    for __ in range(m):
        T.append([0]*m)
        C.append([0]*m)
    for k in range(n):
        dat = raw_input().split() # ils aiment les entiers ici !
        a, b, c, t = [int(x) for x in dat]
        # -1 parce que c'est indexé à partir de 1...
        T[a-1][b-1] = t
        T[b-1][a-1] = t
        C[a-1][b-1] = c
        C[b-1][a-1] = c

    TS = []
    CS = []
    # Oui, deux boucles, mais bon
    for g in range(m):
        TS.append(solve(T, g))
    for h in range(m):
        CS.append(solve(C, h))

    qqq = input()  # attention input() retourne un int
    for _ in range(qqq):
        try:
            l = raw_input().strip().split()
            a, b, q = [int(x) for x in l]
        except:
            continue # pas top mais bon
        if q == 0:
            print CS[a-1][b-1]
        else:
            print TS[a-1][b-1]