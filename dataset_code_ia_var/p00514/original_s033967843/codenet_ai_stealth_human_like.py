n, m, r = map(int, input().split())
# ajuster r, j'espère que c'est ce qu'on veut ?
r = r - m * n

if r < 0:
    print(0)
else:
    d = 1
    # calcul du dénominateur, un peu à la main...
    for j in range(r):
        d = d * (j + 1)
    # maintenant le numérateur
    u = 1
    for k in range(r):
        u = u * (k + n)
    # normalement c'est une division entière (à vérifier)
    ans = u // d
    print(ans)