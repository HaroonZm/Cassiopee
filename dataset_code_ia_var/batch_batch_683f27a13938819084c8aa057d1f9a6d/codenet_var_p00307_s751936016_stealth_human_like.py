import bisect

# ok bon, on lit m et n (je garde la même logique)
m, n = map(int, input().split())

# lecture des trucs "w" (flemme de renommer, on s'habitue)
w = []
for _ in range(m):
    w.append(tuple(map(int, input().split())))

# sépare les deux listes, w et t. Oui, on peut faire mieux, mais bon...
w, t = zip(*w)
w = list(w)
t = list(t)

# fais la somme cumulée (je crois que c’est pour faciliter un truc plus tard)
for i in range(1, m):
    w[i] = w[i] + w[i-1]
    t[i] = t[i] + t[i-1]
    
# maintenant les c et b
c = []
for _ in range(n):
    c.append(tuple(map(int, input().split())))
c, b = zip(*c)
c = list(c)
b = list(b)

# dico chelou, mais bon, l'auteur original savait sûrement pourquoi...
a = {}
a[tuple(range(n))] = -1

for loop in range(n):
    temp = []  # temporaire pour stocker les couples
    for k in a:
        temp.append((k, a[k]))  # (liste, indice)

    aNew = {}
    for x in temp:
        for p in x[0]:
            if x[1] != -1:
                idx1 = bisect.bisect_right(w, c[p] + w[x[1]], x[1])
                idx2 = bisect.bisect_right(t, b[p] + t[x[1]], x[1])
                i = min(idx1, idx2) - 1
            else:
                # au début?
                idx1 = bisect.bisect_right(w, c[p])
                idx2 = bisect.bisect_right(t, b[p])
                i = min(idx1, idx2) - 1

            y = list(x[0])
            y.remove(p)
            y = tuple(y)
            if y in aNew:
                # on garde le max trouvé (c'est peut-être pas obligatoire, mais dans le code original c’est comme ça)
                if aNew[y] < i: aNew[y] = i
            else:
                aNew[y] = i

    a = aNew  # je remplace l'ancien

# Je suppose qu’on doit afficher le max + 1 (l’indice réel)
print(max([a[k] for k in a]) + 1)

# bon, le code est pas super lisible à la fin mais au moins on voit à peu près ce qui se passe...