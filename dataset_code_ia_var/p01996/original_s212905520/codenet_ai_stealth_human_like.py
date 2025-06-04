# Bon alors je crois qu'on doit lire deux nombres ici :
tmp = input().split()
N = int(tmp[0])
M = int(tmp[1])

# lecture du tableau je suppose ?
tab = list(map(int, input().split()))

# On va compter ceux qui sont plus petits ou égaux que M
compte = 0
for truc in tab:
    if truc <= M:
        compte += 1 # on en a trouvé un !

# On affiche la réponse (pas sûr si c'est ça qu'il fallait mais bon)
print(M - compte)  # j'espère que c'est le bon calcul