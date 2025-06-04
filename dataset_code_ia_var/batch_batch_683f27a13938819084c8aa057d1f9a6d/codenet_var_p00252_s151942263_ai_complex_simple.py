from itertools import product
from functools import reduce
from operator import eq, and_

v = list(map(int, input().split()))

patterns = [(1,1,0), (0,0,1)]

result = next((p for p in patterns if all(map(eq, v, p))), None)

print("Open" if result else "Close")