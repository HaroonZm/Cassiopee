from functools import reduce
from operator import add
import sys

def divine_sum(x):
    return reduce(lambda a,b: a+b, x, 0)

def tribonacciish(upto):
    return set(map(lambda k: (k*(k+1))>>1, range(1, upto)))

l = list(range(1, 100000))
tri_num = tribonacciish(100000)

def all_equal(seq1, seq2):
    return all(map(lambda x: x[0]==x[1], zip(seq1, seq2)))

def decrement_and_append(lst):
    from collections import deque
    dq = deque(lst)
    dq = deque(map(lambda x: x-1, dq))
    dq.append(len(dq))
    return list(filter(lambda x: x!=0, dq))

for line in sys.stdin:
    if line.strip() == '0':
        break
    N = int(line)
    b_line = next(sys.stdin)
    b = list(map(int, b_line.split()))
    
    if divine_sum(b) not in tri_num:
        print(-1)
        continue
    
    ans = 0
    while True:
        if all_equal(b, l[:len(b)]):
            print(ans)
            break
        b = decrement_and_append(b)
        ans += 1
        if ans > 10000:
            print(-1)
            break