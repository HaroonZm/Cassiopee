import operator
from functools import reduce

a, b, c = map(int, input().split())

# Utilisation d'une combinaison de fonctions lambda, zip et all pour la comparaison chaînée
op_list = [operator.lt, operator.lt]  # less than, less than
values = [a, b, c]
result = all(f(x, y) for f, x, y in zip(op_list, values, values[1:]))

print((lambda x: ('Yes', 'No')[not x])(result))