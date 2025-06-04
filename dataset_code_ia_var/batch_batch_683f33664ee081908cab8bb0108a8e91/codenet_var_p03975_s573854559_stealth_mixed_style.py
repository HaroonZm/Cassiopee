from functools import reduce

NAB = input().split()
N = int(NAB[0])
A, B = map(int, NAB[1:])

def count_invalid(N, A, B):
    n, c = 0, 0
    while n < N:
        t = int(input())
        if t < A or t >= B:
            c += 1
        n += 1
    return c

def another_way(N, A, B):
    return sum([1 for _ in range(N) if (lambda x: not (A <= x < B))(int(input()))])

def hybrid(N, A, B):
    data = [int(input()) for _ in range(N)]
    filter_func = lambda x: not(A <= x < B)
    return reduce(lambda acc, val: acc + filter_func(val), data, 0)

print(hybrid(N, A, B))