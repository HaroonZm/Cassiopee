from operator import itemgetter

# Lecture optimisée des entrées
values = list(map(int, (input() for _ in range(6))))
x, y = values[:4], values[4:]

# Calcul des résultats avec décomposition
total = sum_x = sum(x)
min_x = min(x)
max_y = max(y)
result = total - min_x + max_y

print(result)