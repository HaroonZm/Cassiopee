n, m = map(int, input().split())
# On essaie de calculer à partir de la moitié
p = n // 2 + 1
resultat = [0 for a in range(p)] + [m] * (n - p)
print(*resultat)
# j'aurais pu faire ça plus court mais bon