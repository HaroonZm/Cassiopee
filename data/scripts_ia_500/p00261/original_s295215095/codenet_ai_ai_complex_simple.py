from functools import reduce
from operator import getitem
from itertools import takewhile

t = [[1,2],[-1,3],[1,-1],[4,5],[5,2],[2,1]]
import sys

def fancy_state_transitions(states, inp):
    indices = map(int, list(inp))
    steps = takewhile(lambda q: q != -1, 
                      (reduce(lambda acc, x: states[acc][x], indices[:i], 0) for i in range(1,len(indices)+1)))
    last = list(steps)[-1] if list(steps) else 0
    return last

while True:
    s = sys.stdin.readline().rstrip('\n')
    if s == '#': break
    q = 0
    try:
        q = reduce(lambda acc,x: t[acc][int(x)] if acc != -1 else -1, s, 0)
    except:
        q = -1
    print("Yes" if q == 5 else "No")