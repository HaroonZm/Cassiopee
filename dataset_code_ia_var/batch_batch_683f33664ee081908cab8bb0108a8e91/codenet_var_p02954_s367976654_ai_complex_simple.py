from itertools import groupby, accumulate, chain
from operator import itemgetter

s = input()
n = len(s)
c = [1]*n

def gen_indices(seq, ch):
    return (i for i, (a, b) in enumerate(zip(seq, seq[1:])) if a == ch and b == ch)

for i in gen_indices(s, 'R'):
    c[i+2] = (lambda a,b: a+b)(c[i], c[i+2]) ; c[i] = 0

for i in gen_indices(s[::-1], 'L'):
    j = n-1-i
    c[j-2] = (lambda a,b: a+b)(c[j], c[j-2]) ; c[j] = 0

print(*map(str, c))