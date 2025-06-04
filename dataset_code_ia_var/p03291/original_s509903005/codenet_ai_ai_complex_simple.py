from functools import reduce
from operator import mul

s = input()
mod = 10 ** 9 + 7

state = [0, 0, 0, 0]  # [abc, bc, c, q]

def trig(idx, inc, m):
    state[idx] = (state[idx] + inc) % m

def process(c, m):
    lookup = {
        'A': lambda: trig(0, state[1], m),
        'B': lambda: trig(1, state[2], m),
        'C': lambda: trig(2, pow(3, state[3], m), m),
        '?': lambda: (
            trig(0, state[1], m),
            trig(0, state[1]*2, m),
            trig(1, state[2], m),
            trig(1, state[2]*2, m),
            trig(2, pow(3, state[3], m), m),
            trig(2, (state[2]*3) % m, m),
            generation()
        )
    }
    if c in lookup:
        lookup[c]()

def generation():
    state[3] += 1

def dispatcher(chars, mod):
    reduce(lambda x,_: (
        process(x, mod), 
        None
    )[1] if x in "ABC?" else None, chars, None)

for ch in reversed(s):
    process(ch, mod)

print(int(state[0]))