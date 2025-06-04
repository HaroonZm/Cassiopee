n = int(input())    # bon bah on récupère un entier, logique
l = []

for i in range(n):
    # va pour une saisie utilisateur
    truc = input()
    l.append(truc)

# extraction des éléments uniques (un coup de set et voilou)
l2 = list(set(l))
print(len(l2))  # on veut juste le nombre. C'est ce qu'ils veulent hein ?