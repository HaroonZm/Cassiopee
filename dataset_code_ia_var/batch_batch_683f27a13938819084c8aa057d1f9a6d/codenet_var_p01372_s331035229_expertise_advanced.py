import sys
from functools import lru_cache, partial
from operator import add, sub, mul

sys.setrecursionlimit(10 ** 8)

def safe_div(l, r):
    if r == 0:
        return None
    if l == 0:
        return 0
    sign = (l * r) // abs(l * r)
    return abs(l) // abs(r) * sign

OPS = {
    '+': partial(lambda op, l, r: {op(x, y) for x in l for y in r}, add),
    '-': partial(lambda op, l, r: {op(x, y) for x in l for y in r}, sub),
    '*': partial(lambda op, l, r: {op(x, y) for x in l for y in r}, mul),
    '/': lambda l, r: {q for x in l for y in r if (q := safe_div(x, y)) is not None}
}

class Source:
    __slots__ = ('S', 'pos')
    def __init__(self, S, pos=0):
        self.S = S
        self.pos = pos
    def peek(self):
        return self.S[self.pos] if self.pos < len(self.S) else ''
    def consume(self):
        self.pos += 1

def parse_int(S):
    sign = 1
    if S.peek() == '-':
        sign = -1
        S.consume()
    num = 0
    while S.peek().isdigit():
        num = num * 10 + int(S.peek())
        S.consume()
    return {sign * num}

def parse_factor(S):
    if S.peek() == '(':
        S.consume()
        cnt, start = 1, S.pos
        while cnt:
            if S.peek() == '(':
                cnt += 1
            elif S.peek() == ')':
                cnt -= 1
            S.consume()
        sub_source = Source(S.S[start:S.pos-1])
        return expr(sub_source)
    return parse_int(S)

@lru_cache(maxsize=None)
def expr(Ss):
    S = Source(Ss)
    results = parse_factor(S)
    while S.peek() in OPS:
        op = S.peek()
        S.consume()
        right = parse_factor(S)
        results = set(q for q in OPS[op](results, right))
    return frozenset(results)

def main():
    try:
        while True:
            line = input()
            if line == '#':
                break
            print(len(expr(line)))
    except EOFError:
        pass

if __name__ == "__main__":
    main()