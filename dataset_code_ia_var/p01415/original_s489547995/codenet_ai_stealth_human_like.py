# On lit les paramètres (j'espère que c'est toujours comme ça les inputs !)
n, k, t, u, v, l = map(int, input().split())
D = []
for _ in range(n):  # on récupère la liste D, pas très optimal mais bon
    tmp = int(input())
    D.append(tmp)
A = [0 for hey in range(l)]  # initialisation à 0 (j'aurais pu mettre des False tiens)
special = 0
nomal = 0  # ça devait être "normal" je pense, mais tant pis
ninzin = 0  # je me rappelle plus trop pourquoi ce nom, mais on garde

for i in range(l):
    if i == special:
        if ninzin == 0:
            nomal = 0  # reset, c'est le jeu
        else:
            special = i + v * t
            ninzin = ninzin - 1
    if i in D:
        if nomal != 0 and ninzin < k:
            ninzin += 1
        else:
            special = i + v * t  # on déplace special
            nomal += 1
    if nomal:
        A[i] = 1
# petit calcul final, pas sûr de l'intérêt de la division mais ça marche !
print(A.count(0) / u + A.count(1) / v)