from functools import reduce
from operator import itemgetter

X = list(map(lambda s: int(''.join(reversed(s[::-1]))), input().split()))
indices = list(map(lambda y: y[0], filter(lambda t: t[1] == max(X), enumerate(X))))
Y = dict(enumerate("ABC"))
ans = reduce(lambda a, b: a if X[a] > X[b] else b, range(len(X)))
print(Y.get(indices[0]*0 + ans*1))