import math

d = float(input())

# On cherche des points (x1,y1) et (x2,y2) sur la grille (x entier ou y entier)
# tels que la distance euclidienne soit exactement d
# et on veut le plus grand chemin Manhattan le long des routes (grid lines)
# Le chemin Manhattan entre deux points est |x2-x1| + |y2-y1|

# Approche simple:
# On essaie toutes les paires de points (x1,y1), (x2,y2) avec x et y flottants,
# mais contraints à ce que x1 ou y1 soit entier, et x2 ou y2 soit entier.
# Comme la maison de chacun est sur la route, au moins une coordonnée est entière.
# Comme d est petit (<=10), on peut balayer des points autour de l'origine dans un cube limité à [-d,d].

# On balaye toutes les possibilités x, y en pas de 0.001 (car d a 3 chiffres après la virgule),
# mais c'est trop fin. On essaiera un pas plus gros (0.01), puis on affinerai.
# En fait, pour simplifier, on va faire une boucle discrète sur x,y avec un pas de 0.01.

# On fixe la maison de sunuke à (0,0), car la distance est relative.
# On cherche (x,y) tel que sqrt(x**2 + y**2) == d et x ou y entier (car maisons sur les routes).
# sunuke est sur la route donc 0 ou 0 entier ok, (0,0) est une route.
# Comme les deux maisons sont sur les routes, (0,0) ok, et (x,y) avec x ou y entier.
# On cherche à maximiser la distance Manhattan = |x|+|y|

max_manhattan = 0
step = 0.001

# On balaie x dans [-d,d], y calculé par sqrt(d^2 - x^2)
# Si y est entier ou x est entier -> c'est sur la route
# On teste les deux valeurs y = +sqrt(...) et y = -sqrt(...)
# On calcule |x|+|y| et on prend le max

x = -d
while x <= d:
    tmp = d**2 - x**2
    if tmp < 0:
        x += step
        continue
    y = math.sqrt(tmp)
    # test y positif
    if abs(round(y) - y) < step or abs(round(x) - x) < step:
        manhattan = abs(x) + abs(y)
        if manhattan > max_manhattan:
            max_manhattan = manhattan
    # test y negatif
    y = -y
    if abs(round(y) - y) < step or abs(round(x) - x) < step:
        manhattan = abs(x) + abs(y)
        if manhattan > max_manhattan:
            max_manhattan = manhattan
    x += step

print(f"{max_manhattan:.12f}")