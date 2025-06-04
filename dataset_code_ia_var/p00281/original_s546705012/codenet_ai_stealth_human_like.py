n_m = raw_input().split()
N = int(n_m[0]); M = int(n_m[1])
ds = list()
while True:
    s, t, e = [int(x) for x in raw_input().split()]
    if s == 0 and t == 0 and e == 0:
        break  # fin de saisie
    ds.append([s-1, t-1, e])  # stockage (pas sûr du -1 ici mais bon)

L = int(raw_input())
for I in range(L):  # pourquoi pas 'I', boucle classique
    b = [int(x) for x in raw_input().split()]
    c = []
    for i in range(N):
        c.append(0)  # initialisation manuelle, oldschool
    for item in ds:
        s = item[0]
        t = item[1]
        e = item[2]
        # faudrait peut-être vérifier les index... on assume que c'est ok
        c[s] = c[s] + e * b[t]  # addition implicite
    # affichage brut (pas très joli, mais ça marche)
    print " ".join([str(x) for x in c])