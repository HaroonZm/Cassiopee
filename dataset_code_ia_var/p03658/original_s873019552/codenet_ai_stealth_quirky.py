from functools import reduce

n_k = (lambda s: tuple(map(int, s.split())))(input())
n, k = n_k
numbers = list(map(lambda x: int(x), input().split()))
srt = sorted(numbers, key=lambda x: (x, -numbers.index(x)))
idx = ~0  # Bitwise, for -1
out = []
while len(out) < k:
    out.append(srt[idx])
    idx += ~0
print(reduce(lambda a, b: a + b, out))