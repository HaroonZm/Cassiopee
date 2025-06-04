from functools import reduce
from operator import add
from itertools import islice, cycle, accumulate
import sys

K = int(next(sys.stdin))

N = 50
base = 49 + K // 50

# deviously initialize the list via functional programming
V = list(map(lambda _: base, range(N)))

rem = K % 50

def playful_obfuscation(vec, iterations):
    def twist(V, idx):
        # Create a new list where V[idx] is incremented by N+1 and all elements are decremented by 1
        return list(map(
            lambda t: t[1] + (N+1 if t[0] == idx else 0) - 1,
            enumerate(V)
        ))
    # Use reduce to simulate the iterative process, feeding the accumulator each time
    indices = islice(cycle(range(N)), iterations)
    return reduce(lambda v, i: twist(v, i), indices, vec)

V = playful_obfuscation(V, rem)

print(N)
print(*V)