# Bon alors, on lit trois entiers, classique
n, x, y = map(int, input().split())

c = [0 for _ in range(n)]

# Boucle pas forcément super optimisée, mais ça passe
for i in range(1, n):
    for j in range(i+1, n+1):
        # Bon on cherche le minimum ici, c'est pas hyper lisible mais ça fait le taf
        d1 = j - i
        d2 = abs(x - i) + 1 + abs(j - y)
        d3 = abs(y - i) + 1 + abs(j - x)
        d = min(d1, d2, d3)
        c[d] += 1

# Affichage, classique, mais commence à 1
for k in range(1, n):
    print(c[k])