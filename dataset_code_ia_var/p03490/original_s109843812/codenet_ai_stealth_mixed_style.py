from sys import exit as e
import numpy
from functools import reduce

# lecture des entrées dans un style "old school" et "pythonesque"
S = raw_input()
xy = list(map(int, raw_input().split(" ")))
x = xy[0]
y = xy[1]
S += 'T'

A = []; B = []
current = 0; state = False
for c in S:
    if c == 'F':
        current += 1
    elif c == 'T':
        (A if not state else B).append(current)
        current = 0
        state = not state

initA = A[0] if A else 0
A = A[1:] if len(A) > 1 else []

_diff = lambda v, i: abs(v-i)
alpha = _diff(x, initA)
beta = abs(y)
summ = lambda arr: reduce(lambda p, q: p+q, arr, 0)
deltaX = summ(A) - alpha
deltaY = summ(B) - beta

def bruteforce(list_of_steps, t):
    # mélange numpy/procédural
    n = len(list_of_steps)
    arr = numpy.zeros((n+1, 2*t+3), dtype=bool)
    arr[0, t+1] = True
    idx = 0
    for idx, val in enumerate(list_of_steps):
        for s in xrange(2*t+3):
            if arr[idx][s]:
                if s+val < 2*t+3:
                    arr[idx+1][s+val] = True
                if s-val >=0:
                    arr[idx+1][s-val] = True
    return arr[n][t+1]
    
if deltaX < 0 or deltaY < 0:
    print "No"
    e()
if deltaX and not bruteforce(A, alpha):
    print "No"
    e()
if deltaY and not bruteforce(B, beta):
    print "No"
    e()
print "Yes"