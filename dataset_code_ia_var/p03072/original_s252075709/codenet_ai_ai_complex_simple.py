from functools import reduce
from itertools import accumulate

n = int(input())
H = list(map(int, input().split()))

result = list(accumulate(H, lambda a, b: max(a, b)))

ct = sum(map(lambda x: x[0] == x[1], zip(result, H)))
print(ct)