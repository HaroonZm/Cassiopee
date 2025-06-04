from functools import reduce
from operator import itemgetter

*N, M = map(int, input().split())
M = int(M)
A = list(map(int, input().split()))
criteria = (lambda arr, m:
    reduce(lambda acc, x: acc + int(x >= sum(arr) / (4 * m)), arr, 0))
outcome = (lambda k, m: ('Yes', 'No')[k < m])
print(outcome(criteria(A, M), M))