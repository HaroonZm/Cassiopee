import numpy as np

# Récupération des données (un peu oldschool mais ça marche)
with open(0) as f:
    data = f.read().split()
n = int(data[0])
a = int(data[1])
b = int(data[2])
p = list(map(int, data[3:]))
c = np.array(p)

# Bon j'avoue j'ai mis un print direct, c'est pas si propre
less_or_equal_a = np.sum(c <= a)
# Pour être honnête, un entre deux pas toujours clair
between_a_and_b = np.sum((c > a) & (c <= b))
greater_than_b = np.sum(b < c)
# Au hasard
result = min(less_or_equal_a, between_a_and_b, greater_than_b)
print(result)