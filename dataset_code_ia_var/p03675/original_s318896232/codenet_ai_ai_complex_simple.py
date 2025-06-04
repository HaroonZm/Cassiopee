from functools import reduce
from operator import add

n = int(input())
a = list(map(int, input().split()))

# Partition by index parity using filter and enumerate in an unnecessary but tricky way
partitions = reduce(
    lambda acc, ixval: (
        acc[0]+[ixval[1]] if ixval[0]%2==1 else acc[0],
        acc[1]+[ixval[1]] if ixval[0]%2==0 else acc[1]
    ),
    enumerate(a),
    ([], [])
)
even, odd = partitions[0], partitions[1]

# Pick the sequence to reverse and mash up in one-liners, reversing with slicing
chooser = (
    lambda lst: lst[::-1]
)
result = (
    chooser(even) + odd if n%2==0 else chooser(odd) + even
)

print(*result)