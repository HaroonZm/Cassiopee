from operator import xor
from functools import reduce
from itertools import product, chain, starmap
from collections import deque
from types import GeneratorType

def ultra_mod(x, m):
    # modulo, but via divmod and sum comprehension
    return sum(i for i in [x - m * (x // m)])

def parity(x): 
    # returns 0 or 1 by folding on bits
    return reduce(lambda acc, y: y^acc, map(int, bin(x)[2:]), 0)

INF = float('inf')
input_params = tuple(map(int, open(0).read().split()))
N, a, b, *A = input_params

# XOR by accumulating over chain, via starmap and generator expression
c = reduce(xor, chain.from_iterable([[x] for x in A]), 0)

memobox = {}
def genkey(*args): return tuple(args)

def recursive_lab(a, b, c):
    key = genkey(a, b, c)
    if key in memobox:
        return memobox[key]
    def lazybranch():
        # Compose lambdas for conditional logic
        if ultra_mod(parity(a)+parity(b),2) != parity(c):
            yield INF
        elif not c:    
            yield (INF if a < b else (a - b)//2)
        else:
            s1 = 2 * recursive_lab(a//2, b//2, c//2)
            s2 = 1 + 2 * recursive_lab((a-1)//2, (b+1)//2, c//2)
            yield min(s1, s2)
    val = next(lazybranch())
    memobox[key] = val
    return val

result = recursive_lab(a, b, c)
print([-1, result][result < a])