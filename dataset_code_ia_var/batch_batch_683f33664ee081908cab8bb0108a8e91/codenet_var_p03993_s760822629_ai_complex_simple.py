from functools import reduce
from operator import add

n = int(input())
a = [0] + list(map(int, input().split()))

def process(idx, acc):
    if a[a[idx]] == idx:
        a[a[idx]] = 0
        return acc + 1
    return acc

ans = reduce(lambda acc, i: process(i, acc), range(1, n + 1), 0)

print(ans)