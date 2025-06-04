# Entrée des valeurs pour h1 et h2
inputs = input().split()
h1 = int(inputs[0])
h2 = int(inputs[1])

# Entrée des valeurs pour k1 et k2
inputs = input().split()
k1 = int(inputs[0])
k2 = int(inputs[1])

# Entrée des valeurs pour a, b, c, d
inputs = input().split()
a = int(inputs[0])
b = int(inputs[1])
c = int(inputs[2])
d = int(inputs[3])

# Calcul des points pour hiroshi
p1 = a * h1 + c * (h1 // 10) + b * h2 + d * (h2 // 20)

# Calcul des points pour kenjiro
p2 = a * k1 + c * (k1 // 10) + b * k2 + d * (k2 // 20)

# Comparaison des scores et affichage du résultat
if p1 > p2:
    print("hiroshi")
elif p1 < p2:
    print("kenjiro")
else:
    print("even")