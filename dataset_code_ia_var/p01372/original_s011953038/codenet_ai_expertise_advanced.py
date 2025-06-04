import sys
from functools import lru_cache
from operator import add, sub, mul, floordiv
import re

sys.setrecursionlimit(10**7)
INF = float('inf')
EPS = 1e-13
MOD = 10**9 + 7
D4 = [(-1,0),(0,1),(1,0),(0,-1)]
D8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [x-1 for x in LI()]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip('\n')
def pf(s): print(s, flush=True)

OPS = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x/y) if y else None}

def tokenize(expr):
    # Split formula into numbers and operators for generalized parsing
    return [int(token) if token.isdigit() else token
            for token in re.findall(r'\d+|[()+\-*/]', expr)]

def main():
    results = []
    while True:
        line = S()
        if line == '#':
            break

        tokens = tokenize(line)
        n = len(tokens)

        @lru_cache(maxsize=None)
        def dfs(l, r):
            # Returns a set of possible results for subexpression tokens[l:r]
            if l+1 == r:
                return {tokens[l]} if isinstance(tokens[l], int) else set()

            res = set()
            # Handle parenthesis
            if tokens[l] == '(' and tokens[r-1] == ')':
                # check matching
                cnt = 0
                for i in range(l, r):
                    if tokens[i] == '(': cnt += 1
                    elif tokens[i] == ')': cnt -= 1
                    if cnt == 0 and i < r-1:
                        break
                else:
                    return dfs(l+1, r-1)

            # Try every operator at depth 0 (not inside parens)
            depth = 0
            for i in range(l, r):
                tok = tokens[i]
                if tok == '(': depth += 1
                elif tok == ')': depth -= 1
                elif depth == 0 and tok in OPS:
                    left = dfs(l, i)
                    right = dfs(i+1, r)
                    op = OPS[tok]
                    for x in left:
                        for y in right:
                            if tok == '/':
                                if y == 0: continue
                                v = -(abs(x)//abs(y)) if x*y<0 else x//y
                            else:
                                v = op(x, y)
                            res.add(v)
            return res

        ans = len(dfs(0, n))
        results.append(ans)
    return '\n'.join(map(str, results))

print(main())