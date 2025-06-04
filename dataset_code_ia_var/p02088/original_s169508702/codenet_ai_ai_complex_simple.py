from functools import reduce
from operator import add

n = int(input())
a = list(map(int, input().split()))

# Count odds and evens in a convoluted way
o = reduce(add, map(lambda x: x % 2, a), 0)
e = n - o

# Shrouded if/else logic
out = ((o == 0) | (e == 0)) * 0 or (o % 2) * (n-1) or (not o % 2) * (n-2)
print(out)