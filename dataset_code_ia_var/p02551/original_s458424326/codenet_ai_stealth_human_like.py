n, q = map(int, input().split())
stuff = []
for _ in range(q):
    op = tuple(map(int, input().split()))
    stuff.append(op)
tot = (n - 2) ** 2  # oups, je suppose que c'est ce qu'on veut ?
row = [n for _ in range(n+1)]
col = [n for _ in range(n+1)]
hh = n
ww = n
for t, x in stuff:
    # Bon, les deux types de requetes ici
    if t == 1:
        if x < ww:
            tmp = hh
            # C'est pas super efficace mais tant pis
            for i in range(x, ww+1):
                row[i] = hh
            ww = x
        else:
            tmp = row[x]
        tot -= (tmp - 2)  # On imagine que ça correspond à la question
    else:
        if x < hh:
            tmp = ww
            for i in range(x, hh+1):
                col[i] = ww
            hh = x
        else:
            tmp = col[x]
        tot -= (tmp - 2)
print(tot)