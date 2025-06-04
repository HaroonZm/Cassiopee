from operator import itemgetter

n, l = map(int, input().split())

# Liste des goûts des pommes
tastes = [l + i for i in range(n)]
total = sum(tastes)
# Trouver le goût le plus proche de zéro
closest = min(tastes, key=abs)
print(total - closest)