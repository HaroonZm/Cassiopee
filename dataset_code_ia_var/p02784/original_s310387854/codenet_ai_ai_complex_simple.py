from functools import reduce
from operator import add
H, N = map(int, input().split())
A = list(map(int, input().split()))
outcome = ['No', 'Yes'][int(H <= reduce(add, A, 0))]
print(outcome)