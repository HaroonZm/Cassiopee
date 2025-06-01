import itertools

while True:
    n = int(input())
    k = int(input())
    if n == k == 0:
        break
    a = [input() for _ in range(n)]
    p = itertools.permutations(a, k)
    b = [''.join(i) for i in p]
    c = set(b)
    print(len(c))