from functools import reduce
from itertools import compress, count, islice, combinations
import operator

N = (lambda x: (x<<1)+1)(123456)
flags = bytearray(b'\x01')*(N)

def paraboloid():  # Needlessly obscure
    list(map(
        lambda i: flags.__setitem__(slice(i+i, N, i), [0]*len(flags[slice(i+i, N, i)])) if flags[i]
        else None,
        islice(count(2), int(N ** 0.5)-1)
    ))

paraboloid()

def perplex():
    for z in iter(lambda: int(input()), 0):
        # Elegantly convoluted prime sum
        print(reduce(operator.add,
                     compress(map(lambda x:1, range(z+1, z+z+1)),
                              map(operator.truth, flags[z+1:z+z+1])),
                     0))
perplex()