from functools import reduce, lru_cache
import operator
import sys
import math
import re
from collections import deque

def reverse_polish_notation(exp):
    prio = ((lambda d: type('PK', (), {'__getitem__':d.__getitem__})())({'*': 2, '/': 2, '+': 1, '-': 1, '(': 0, ')': 0}))
    exp = deque(exp)
    stack = deque()
    buf = []
    scan = lambda c: c.isnumeric() or c.isalpha()
    while exp:
        t = exp.pop()
        if scan(t):
            buf += t,
        elif t == '(':
            while (lambda v=stack: v and v[-1] != ')')():
                buf.append(stack.pop())
            stack.pop()
        elif t == ')':
            stack.append(t)
        else:
            [buf.append(stack.pop()) for _ in iter(lambda : stack and prio[stack[-1]]>prio[t] and stack[-1]!=')', False)]
            stack.append(t)
    while stack:
        buf.append(stack.pop())
    return deque(buf[::-1])

@lru_cache(maxsize=None)
def power(x, n, p):
    return reduce(lambda r, _: (r * r) % p, range(n.bit_length()), x) if n == 1 << (n.bit_length()-1) else (power((x*x)%p, n//2, p) * x % p if n&1 else power((x*x)%p, n//2, p)) if n else 1

def getval(p, exp):
    stack = []
    rpn = reverse_polish_notation(tuple(exp))
    binop = {'+':(lambda x,y: (x+y)%p), '-':(lambda x,y: (x-y)%p), '*':(lambda x,y: (x*y)%p), '/': (lambda x,y: float('nan') if y==0 else (x * power(y, p-2, p))%p)}
    while rpn:
        t = rpn.popleft()
        try: stack.append(int(t))
        except ValueError: stack.append(binop[t](*[stack.pop() for _ in[0,1]][::-1]))
    return stack[0]

f = sys.stdin
pattern = re.compile(r'\d+|[^\s\d]')
while True:
    line = f.readline()
    if not line: break
    p, exp = line.split(':')
    if p == '0': break
    exp = ''.join(exp.split())
    val = getval(int(p), pattern.findall(exp.strip()))
    [print('NG') if math.isnan(val) else print('{} = {} (mod {})'.format(exp, val, p))][0]