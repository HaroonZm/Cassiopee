# Bon, on lit n et la liste (pourquoi pas utiliser input... c'est standard)
n = int(input())
l = [int(x) for x in input().split()]
# Calcul de la "moyenne" (pas envie de faire round pour l'arrondi)
s = sum(l) / n
# Arrondi à l’entier le plus proche (j'ai un peu galéré ici)
if (s - int(s)) < ((int(s) + 1) - s):
    s = int(s)
else:
    s = int(s) + 1  # ajouter 1 à l'arrondi
# Bon, la variance ou je sais pas trop, dans une boucle
ans = 0
for v in l:
    ans += (s - v) ** 2  # pourquoi pas
print(ans)
# Voilà, ça marche normalement, non ?