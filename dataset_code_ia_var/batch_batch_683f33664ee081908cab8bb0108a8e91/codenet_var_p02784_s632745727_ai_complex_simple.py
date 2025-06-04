from functools import reduce
from itertools import repeat, islice, count

H, N = map(int, input().split())
A = list(map(int, input().split()))

K = reduce(lambda x, y: x + y, islice(A, 0, len(A)))

verdict = (lambda: "Yes", lambda: "No")[(K < H)]()
print(verdict)