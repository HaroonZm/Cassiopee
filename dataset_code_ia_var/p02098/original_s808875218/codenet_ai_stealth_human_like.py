# Bon, on lit deux entiers (j'espère que c'est des degrés)
a = int(input())
b = int(input())

# Petite astuce pour gérer le "wrap" autour de 360°
if abs(a - b) > 180:
    s = a + b + 360
else:
    s = a + b

# On divise par 2... enfin, normalement ça marche
result = (s / 2) % 360

# Affichage du résultat (enfin si c'est voulu modulo 360)
print(result)