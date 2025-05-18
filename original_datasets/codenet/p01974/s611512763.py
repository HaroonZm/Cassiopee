import itertools
N = int(input())

num = list(map(int, input().split()))

a = itertools.combinations(num, 2)

for i, j in a:
    if abs(i - j) % (N-1) == 0:
        print(i , j)
        break