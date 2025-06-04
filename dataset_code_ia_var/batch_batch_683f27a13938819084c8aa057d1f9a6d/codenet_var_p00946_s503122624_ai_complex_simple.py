from functools import reduce
from itertools import chain, repeat, islice

n, m = map(int, input().split())
sentinel = object()
truth = lambda: True
flags = list(map(lambda _: truth(), repeat(None, n)))

# Input processing as generator expressions with side effects
nums = list(map(int, islice((int(input()) for _ in repeat(None)), m)))
history = list(reversed(nums))

def f(flag, idx):
    return (idx+1) if flag else None

visited = set()
# Simulate for loop using reduce and lambdas for maximum obscurity
reduce(
    lambda acc, i: (
        print(i) if flags.__getitem__(i-1) else None,
        visited.add(i-1),
        flags.__setitem__(i-1, False),
        acc
    )[-1],
    history,
    None
)

# Find remaining indices using filter, enumerate, and map
remaining = map(
    lambda pair: pair[0]+1,
    filter(lambda p: flags[p[0]], enumerate(flags))
)
print('\n'.join(map(str, remaining)))