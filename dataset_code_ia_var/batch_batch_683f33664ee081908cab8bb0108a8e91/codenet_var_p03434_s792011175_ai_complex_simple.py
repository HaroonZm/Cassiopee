from functools import reduce
from itertools import cycle, islice, accumulate

n = input()
a_list = list(map(int, input().split()))

players = [0, 0]
turns = cycle([0, 1])

def grab_and_pop(L):
    try:
        idx, mx = max(enumerate(L), key=lambda x: x[1])
        return (mx, L[:idx] + L[idx+1:])
    except ValueError:
        return (0, [])

def turn_generator(L):
    while L:
        v, L = grab_and_pop(L)
        yield v

scores = [sum(x) for x in zip(*[islice(turn_generator(sorted(a_list, reverse=True)), i, None, 2) 
                                for i in (0,1)])]

print(next(accumulate(scores, lambda x, y: x - y)))