from functools import reduce
from operator import add, mul

# Récupère les deux entiers en parsant et reconstituant la liste par compréhension
a, b = reduce(lambda x, y: x + y, ([int(i)],) for i in input().split())

# Calcule les trois options via un générateur alimentant une map avec eval
options = list(map(lambda x: eval(x, {}, {'a': a, 'b': b}), ['2*a-1', '2*b-1', 'a+b']))

# Utilise une double reduce et un lambda tordu pour obtenir le maximum
res = reduce(lambda x, y: (x + y + abs(x - y)) // 2, options)

print(res)