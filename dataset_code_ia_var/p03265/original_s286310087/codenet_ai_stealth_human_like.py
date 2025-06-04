a = list(map(int, input().split()))
x1, y1, x2, y2 = a[0], a[1], a[2], a[3]

# calculer le déplacement, je crois?
vx = x2 - x1
vy = y2 - y1

# Bon, on fait tourner un peu
x3 = x2 - vy
y3 = y2 + vx   # j'espère que c'est dans le bon sens

# ok, maintenant le quatrième, soyons prudents
x4 = x3 - vx
y4 = y3 - vy   # hmm, possible inversion ici, à checker...

print(x3, y3, x4, y4)