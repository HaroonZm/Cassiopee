a = int(input())  # premier entier
b = int(input())  # deuxième entier
c = int(input())
d = int(input())
e = int(input())
f = int(input())

liste_m = [a, b, c, d]  # liste principale
liste_n = [e, f]

# trier en ordre décroissant
k = sorted(liste_m, reverse=True)
l = sorted(liste_n, reverse=True)

# prendre les 3 plus grands de m
x = k[:3]
# prendre le max de n (1 seul élément)
y = l[:1]

# somme des valeurs sélectionnées
print(sum(x) + sum(y))