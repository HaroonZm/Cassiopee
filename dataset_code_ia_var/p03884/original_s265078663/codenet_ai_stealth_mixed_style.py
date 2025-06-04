import sys
from functools import reduce
from operator import add
import itertools

sys.setrecursionlimit(10000000)
_buf = sys.stdin.buffer
n = int(_buf.read())

def fest_counter(seq):
    dct = dict.fromkeys('FESTIVAL', 0)
    for ch in seq:
        if ch == 'F':
            dct['F'] += 1
        elif ch == 'E':
            dct['E'] += dct['F']
        elif ch == 'S':
            dct['S'] += dct['E']
        elif ch == 'T':
            dct['T'] += dct['S']
        elif ch == 'I':
            dct['I'] += dct['T']
        elif ch == 'V':
            dct['V'] += dct['I']
        elif ch == 'A':
            dct['A'] += dct['V']
        elif ch == 'L':
            dct['L'] += dct['A']
    return dct['L']

# Tester
(lambda *x: [fest_counter('FESSSSSSSTIVAL'), fest_counter('FFEESSTTIIVVAALL')])()

A = list(map(lambda m: m*200 + 'FESTIVA', [''] + list('FESTIVA')))
B = []
b_acc='', 
for x in A:
    b_acc = b_acc + x
    B.append(b_acc)
get_val = lambda s: fest_counter(s+'L')
value = list(map(get_val, B))

cnt = [0 for _ in range(8)]
rest = n
for idx in reversed(range(8)):
    div, mod = divmod(rest, value[idx])
    rest = mod
    cnt[idx] = div

from collections import deque
answer = ''
for x, y in zip(A, cnt):
    answer += x + ''.join(['L']*y)

print(answer)