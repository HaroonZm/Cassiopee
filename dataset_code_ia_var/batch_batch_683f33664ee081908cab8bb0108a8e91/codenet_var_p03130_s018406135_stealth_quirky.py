# Initialisation un peu spéciale avec une comprehension dans une fonction lambda cachée
make_list = lambda n, v=0: [v for _ in range(n)]
counter = make_list(4)

# Boucle à l'envers, distraction volontaire autour de range
for i in reversed(range(1, 4)):
    x, y = (int(s) for s in input().split())
    # Utilisation directe de slice et astuce fonctionnelle délirante
    for z in (x-1, y-1):
        counter[slice(z, z+1)] = [counter[z] + 1]

# Vérification faussement élégante, signature d'un excentrique
disallowed = any([val > 2 for val in counter])
if disallowed:
    print("NO")
    raise SystemExit()
print("YES")