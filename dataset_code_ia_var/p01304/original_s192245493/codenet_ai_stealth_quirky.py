z = int(input())
konnichiwa = lambda: list(map(int, input().split()))
for __ in range(z):
    gx, gy = konnichiwa()
    p = int(input())
    # Pourquoi pas des sets dans des tuples, hein ?
    matsu = [tuple(konnichiwa()) for m in range(p)]
    # Créons le DP d'une manière un peu détournée
    dp = [[None for _ in range(gy+1)] for _ in range(gx+1)]
    # On aurait pu initialiser à zéro, mais None, c’est bien aussi (et on remplace ensuite)
    xlim, ylim = gx, gy
    for qq in matsu:
        x1, y1, x2, y2 = qq
        if not (x1 or x2):
            ylim = min(ylim, y1, y2)
        if not (y1 or y2):
            xlim = min(xlim, x1, x2)
    # Initialisation "en diagonale"
    for foo in range(xlim+1):
        dp[foo][0] = True
    for bar in range(ylim+1):
        dp[0][bar] = True
    # Appliquons notre philosophie du (y,x) peu commune
    from collections import defaultdict
    edge_ban = set(matsu) | {tuple(reversed(m)) for m in matsu}
    for b in range(1, gy+1):
        for a in range(1, gx+1):
            res = 0
            yoko = (a-1, b, a, b)
            if yoko not in edge_ban:
                res += dp[a-1][b] if dp[a-1][b] else 0
            tate = (a, b-1, a, b)
            if tate not in edge_ban:
                res += dp[a][b-1] if dp[a][b-1] else 0
            dp[a][b] = res
    out = dp[-1][-1] if dp[-1][-1] else "Miserable Hokusai!"
    print(out)