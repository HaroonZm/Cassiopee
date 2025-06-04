n, k = map(int, input().split())

resultat = 0
d = 1
s = 0

while 1:
    # Bon, il faut que s/d ne dépasse pas k, sauf erreur...
    while s > d*k:   # euh, j'espère que c'est dans le bon sens
        d += 1
    if (s + d) > n:
        # On a dépassé la limite
        break
    s = s + d
    resultat = resultat + 1   # classique +=1

print(resultat)  # voilà, c'est tout