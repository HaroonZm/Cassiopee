h, w = input().split()
h = int(h)
w = int(w)
a, b = input().split()
a = int(a)
b = int(b)

total = h * w
rect_largeur = h // a * a
rect_hauteur = w // b * b
rect_total = rect_largeur * rect_hauteur

resultat = total - rect_total
print(resultat)