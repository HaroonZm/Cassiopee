def reverse_polish_notation(exp):
    priority = {'+':0,'-':0,'/':1,'*':1}
    exp = deque(exp)
    stack = deque()
    buffer = deque()
    
    while len(exp):
        token = exp.pop()
        if token.isnumeric():
            buffer.append(token)
        elif token == '(':
            while True:
                token = stack.pop()
                if token == ')':
                    break
                buffer.append(token)
        elif token == ')':
            stack.append(token)
        else:
            while len(stack):
                if stack[-1] == ')' or priority[stack[-1]] <= priority[token]:
                    break
                buffer.append(stack.pop())
            stack.append(token)
    
    while len(stack):
        buffer.append(stack.pop())
        
    return buffer    

def power(x, n, p):
    if n == 0:
        return 1
    res = power(x * x % p, n // 2, p)
    if n & 1:
        res = res * x % p
    return res

from collections import deque
def getval(p, exp):
    exp = reverse_polish_notation(exp)
    stack = deque()
    while len(exp):
        token = exp.popleft()
        if token.isnumeric():
            stack.append(int(token))
        else:
            a, b = stack.pop(), stack.pop()
            if token == '+':
                stack.append((a + b) % p)
            elif token == '-':
                stack.append((a - b) % p)
            elif token == '*':
                stack.append((a * b) % p)
            elif token == '/':
                if b == 0:
                    stack.append(float('nan'))
                else:
                    stack.append((a * power(b, p - 2, p)) % p)

    return stack.pop()

import sys
import math
import re
f = sys.stdin

pattern = re.compile('(\d+|\D)')
while True:
    p, exp = f.readline().split(':')
    if p == '0':
        break
    exp = ''.join(exp.split()).strip()
    
    val = getval(int(p), pattern.findall(exp))
    if math.isnan(val):
        print('NG')
    else:
        print('{} = {} (mod {})'.format(exp, val, p))