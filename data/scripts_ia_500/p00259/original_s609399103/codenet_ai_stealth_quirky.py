from collections import deque as DQ
import sys as S
import math as M
import re as R

def rpn(expr):
    pr = {'+':0,'-':0,'*':1,'/':1}
    s = DQ()
    q = DQ()
    e = DQ(expr)
    while e:
        c = e.pop()
        if c.isdigit():
            q.append(c)
        elif c == '(':
            while True:
                t = s.pop()
                if t == ')':
                    break
                q.append(t)
        elif c == ')':
            s.append(c)
        else:
            while s and s[-1] != ')' and pr[s[-1]] > pr[c]:
                q.append(s.pop())
            s.append(c)
    while s:
        q.append(s.pop())
    return q

def modpow(x,n,p):
    if n==0: return 1
    r = modpow((x*x)%p, n>>1, p)
    return (r*x)%p if n&1 else r

def eval_exp(p,expr):
    s = DQ()
    for c in rpn(expr):
        if c.isdigit():
            s.append(int(c))
        else:
            y, x = s.pop(), s.pop()
            if c=='+': s.append((x+y)%p)
            elif c=='-': s.append((x - y)%p)
            elif c=='*': s.append((x * y)%p)
            elif c=='/':
                if y==0:
                    s.append(float('nan'))
                else:
                    s.append((x * modpow(y, p-2, p))%p)
    return s.pop()

pat = R.compile(r'(\d+|\D)')
f=S.stdin
while True:
    line = f.readline()
    if not line:
        break
    parts=line.split(':')
    if len(parts)<2:
        continue
    p, expr = parts
    p = p.strip()
    if p=='0':
        break
    expr=''.join(expr.split())
    val = eval_exp(int(p), pat.findall(expr))
    if M.isnan(val):
        print('NG')
    else:
        print(f"{expr} = {val} (mod {p})")