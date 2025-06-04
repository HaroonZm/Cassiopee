import itertools
X = [int(el) for el in input().split(' ')]
if X[0] % X[1] == 0:
    print(-1)
else:
    print(X[0])