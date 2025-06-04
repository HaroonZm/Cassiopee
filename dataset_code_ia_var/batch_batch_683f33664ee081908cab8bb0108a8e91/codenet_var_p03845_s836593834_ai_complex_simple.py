from functools import reduce
from operator import add

n = int(input())
t = list(map(int, input().split()))

S = reduce(add, t)
m = int(input())

def change_sum(index, value):
    return S + value - t[index - 1]

queries = [tuple(map(int, input().split())) for _ in range(m)]
get_sum = lambda ab: change_sum(*ab)
ans = list(map(get_sum, queries))

print('\n'.join(map(str, ans)))