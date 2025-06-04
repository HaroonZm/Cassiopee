import itertools

n = int(input())
num = [i for i in range(1, n + 1)]

for per in itertools.permutations(num):
    print(' '.join(str(p) for p in per))