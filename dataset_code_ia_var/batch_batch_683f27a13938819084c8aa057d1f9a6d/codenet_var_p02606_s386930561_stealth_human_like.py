# Bon, on va compter le nombre de nombres divisibles, hein...
L, R, d = input().split()
L = int(L)
R = int(R)
d = int(d)
total = 0

# Boucle un peu classique (y'aurait sûrement mieux mais bon)
while L <= R:
    if (L % d == 0):
        total = total + 1
    L = L + 1 # avance à la prochaine valeur

# Affiche le total (peut-être fallait-il retourner, mais j'affiche !)
print(total)