# On lit d'abord les entrées, ça doit être trois entiers sur la même ligne
vals = input().split()
X = int(vals[0])
A = int(vals[1])
B = int(vals[2])

n = int(input())
L = []
for _ in range(n):
    t = input()
    L.append(t)  # on pourrait tout faire en compréhension, mais bon

for elem in L:
    if elem == 'nobiro':
        X = X + A    # j'aime mieux l'écriture explicite
    elif elem == 'tidime':
        X += B
    else:
        X = 0  # ici c'est un peu radical mais c'est la consigne ?
    if X < 0:
        X = 0 # Bon, pas de négatif du tout

print(X) # résultat final