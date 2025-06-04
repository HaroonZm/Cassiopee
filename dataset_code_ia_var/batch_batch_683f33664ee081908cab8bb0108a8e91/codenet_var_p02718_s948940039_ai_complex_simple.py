from functools import reduce
from itertools import compress, repeat, starmap

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = reduce(lambda x, y: x + y, A)
criteria = list(starmap(lambda a, s, m: a*4*m >= s, zip(A, repeat(S), repeat(M))))
c = sum(list(compress(repeat(1, N), criteria)))
print(["No", "Yes"][(lambda x, y: x >= y)(c, M)])