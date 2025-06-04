from numpy import zeros
from functools import reduce
from itertools import cycle, islice

A, B = map(lambda x: int(''.join(x)), zip(*(input().split(),)))
X = zeros([100,100], dtype=int)

list(map(lambda y: X.__setitem__((slice(None), 99), 1), range(1)))

list(map(lambda i: X.__setitem__((99-i*2, slice(1, None)), [1]*99), range(20)))

def drop_squares(ct, startp, startq, dx, dy, trigger, reset_p, step_f):
    state = [startp, startq]
    for _ in range(ct-1):
        X[state[1],state[0]] = 1
        state[0] += dx
        if state[0]==trigger:
            state[0]=reset_p
            state[1]+=dy
    return None

drop_squares(A,97,98,-2, -2, 3, 97, lambda p,q: (97,q-2))
drop_squares(B,1,1,2,2,95,1, lambda p,q: (1,q+2))

print(*[100,100])
list(map(lambda row: print(reduce(lambda a,b: a+b, map(lambda v: '#.'[v==0], row))), X))