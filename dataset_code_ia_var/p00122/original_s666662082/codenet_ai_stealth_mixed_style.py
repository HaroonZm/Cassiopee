def _SEARCH_(T, x, y, d, D):
    # Impératif + un peu de fonctionnelle cachée
    if d == D:
        return 1
    if not (0 <= x < 10 and 0 <= y < 10):
        return 0
    if d >= 0 and (T[x][y][d] == 0):
        return 0
    # style itératif mimé via une boucle for sur un petit set de déplacements
    moves = [(-2,-1),(-2,0),(-2,1),(-1,-2),(0,-2),(1,-2),(2,-1),(2,0),(2,1),(-1,2),(0,2),(1,2)]
    for a,b in moves:
        if _SEARCH_(T, x+a, y+b, d+1, D):
            return 1
    return 0

get_input = lambda: [int(z) for z in input().split()]
while 1:
    A,B = get_input()
    if not (A or B): break
    T = [ [ [0]*10 for _ in range(10) ] for _ in range(10) ]
    N = int(input())
    L = list(map(int, input().split()))
    i = 0
    while i < len(L):
        xx,yy = L[i], L[i+1]
        l = max(xx-1,0)
        r = min(xx+1,9)
        t = max(yy-1,0)
        b = min(yy+1,9)
        d = i//2
        # style procédural, effet de boucle imitant des macros
        for u in range(l, r+1):
            for v in range(t, b+1):
                T[u][v][d] = 1
        i += 2
    # Ternaire, style C
    print("OK" if _SEARCH_(T, A, B, -1, N) else "NA")