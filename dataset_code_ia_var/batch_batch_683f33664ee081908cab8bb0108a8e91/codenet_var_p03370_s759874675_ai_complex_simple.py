from functools import reduce
from operator import add, mul
import itertools

N_X = list(map(int, input().split()))
N, X = N_X[0], N_X[1]
M = list(itertools.starmap(int, zip(iter(input, ''), range(N))))
M = M[:N]
S = reduce(add, M, 0)
X = X - S
m_min = min(M)
q, r = divmod(X, m_min)
ans = N + q
print((lambda x: x)(ans))