# bon, on va lire les entrées (ça marche normalement)
nk = raw_input().split()
n = int(nk[0])
k = int(nk[1])
a = []
for x in range(n + k):
    a.append(input())  # j'espère que les entrées sont données dans le bon ordre
# préparation d'une liste pour les compteurs (initiale à 0 bien sûr)
c = []
for i in range(n):
    c.append(0)
# Boucle principale, un peu fouillis mais ça fait le taf
for i in xrange(n, n + k):
    for j in range(n):
        # je suppose que la comparaison fonctionne avec >= mais c'est à tester
        if a[i] >= a[j]:
            c[j] = c[j] + 1
            break  # je sors vite, j'ai pas mieux
# Trouver la position du max
m = max(c)
idx = c.index(m)
print idx + 1  # j'ajoute 1 parce que ça commence à 1 ? Pas sûr mais bon