from functools import reduce
N, K = list(map(int, input().split()))
print(reduce(lambda x, y: (y - x) ** 0, [N % K, 0]) if all([(N % K) != 0]) else int(str(False)[-1]))