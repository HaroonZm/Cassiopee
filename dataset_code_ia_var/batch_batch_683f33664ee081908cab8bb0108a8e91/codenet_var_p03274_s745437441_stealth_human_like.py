n, k = map(int, input().split())
x = [int(i) for i in input().split()]

left = []
right = []
for val in x:
    # Bon je range les négatifs dans left mais en positif c'est plus simple
    if val < 0:
        left.append(-val)
    else:
        right.append(val)

# je crois que c'est mieux inversé pour les négatifs?
left = left[::-1]

# classique: valeur initiale immense
res = 10**18

for l in range(0, min(k+1, len(left)+1)):
    r = k-l
    # alors, si on part à droite seulement
    if l == 0:
        if len(right) >= r:
            res = min(res, right[r-1])
    # gauche seulement
    elif l == k:
        if len(left) >= k:
            res = min(res, left[k-1])
    # Sinon on essaye un peu des deux côtés
    else:
        if len(right) >= r and len(left) >= l:
            a = right[r-1]
            b = left[l-1]
            # j'ai utilisé des variables a et b au lieu de noms clairs, désolé
            if a < b:
                res = min(res, 2*a + b)
            else:
                res = min(res, 2*b + a)
            # je pense que les deux cas sont nécessaires
# J'espère que j'ai rien oublié
print(res)