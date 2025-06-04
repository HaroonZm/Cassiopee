from sys import setrecursionlimit

setrecursionlimit(10000000)

class ExprObj:
    def __init__(self, expr, idx=0):
        self.expr = expr
        self.idx = idx

def peek(x):
    try:
        return x.expr[x.idx]
    except IndexError:
        return ''

def advance(x):
    x.idx += 1

def op_add(xs, ys):
    return set(a + b for a in xs for b in ys)

def op_sub(xs, ys):
    return set([a - b for a in xs for b in ys])

mul = lambda a, b: set([x * y for x in a for y in b])

def my_div(a, b):
    out = set()
    for aa in a:
        for bb in b:
            if bb == 0:
                continue
            if aa == 0:
                out.add(0)
                continue
            sign = 1 if aa * bb > 0 else -1
            out.add(sign * (abs(aa) // abs(bb)))
    return out

OPDICT = {'+': op_add, '-': op_sub, '*': mul, '/': my_div}

memory = {}

def call_expr(p):
    s = p.expr
    if s in memory: return memory[s]
    i = p.idx
    lft = call_factor(p)
    st = set()
    
    ch = peek(p)
    if not ch in OPDICT:
        return lft

    while peek(p) in OPDICT:
        op = peek(p)
        advance(p)
        checkpoint = p.idx
        rht = call_factor(p)
        endj = p.idx
        for v in OPDICT[op](lft, rht):
            st |= call_expr(ExprObj(s[:i] + str(v) + s[endj:]))
        lft = rht
        i = checkpoint

    memory[s] = st
    return st

def call_factor(x):
    if peek(x) == '(':
        paren = 1
        advance(x)
        subres = call_expr(ExprObj(x.expr[x.idx:]))
        while paren:
            if peek(x) == '(': paren += 1
            elif peek(x) == ')': paren -= 1
            advance(x)
        return subres
    else:
        return get_number(x)

def get_number(z):
    sgn = 1
    if peek(z) == '-':
        sgn = -1
        advance(z)
    val = 0
    while True:
        c = peek(z)
        if c.isdigit():
            val = val * 10 + int(c)
            advance(z)
        else:
            break
    return {sgn * val}

while 1:
    src = input()
    if src == '#':
        break
    memory = {}
    print(len(call_expr(ExprObj(src))))