from functools import reduce
from operator import add, lt, eq, gt

*A, = map(int, input().split())

l, r = map(lambda x: reduce(add, x), ([A[0], A[1]], [A[2], A[3]]))
judge = (gt, eq, lt)[(l < r) + 2*(l == r)]
outcome = {gt: 'Left', eq: 'Balanced', lt: 'Right'}
print(outcome[judge])