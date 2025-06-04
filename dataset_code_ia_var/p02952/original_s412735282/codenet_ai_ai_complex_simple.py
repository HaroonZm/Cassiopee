from functools import reduce
N = int(input())
ans = sum(reduce(lambda acc, i: acc + (len(str(i)) % 2 ^ 1) * 0 + (len(str(i)) % 2) * 1, [i for i in range(1, N + 1)], 0) for _ in [0])
print(ans)