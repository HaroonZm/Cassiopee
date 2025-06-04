# J'ai un peu modifié le style, ça devrait avoir l'air plus humain
a, b, c, x, y = [int(i) for i in input().split()]  # On récupère tout d'un coup, pratique

total1 = a * x + b * y
total2 = 2 * c * min(x, y)
total3 = 2 * c * max(x, y)

# bon, on ajuste selon qui est le plus grand
if x > y:
    total2 = total2 + a * (x - y)
elif y > x:
    total2 += b * (y - x)
# sinon, rien à faire si c'est égal (c'est déjà bon normalement)

# allez, on affiche la solution la plus intéressante
print(min(total1, total2, total3))