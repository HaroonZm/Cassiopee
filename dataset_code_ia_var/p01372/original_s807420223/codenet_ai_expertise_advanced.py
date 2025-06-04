#!/usr/bin/env python3

import sys
import re
from functools import lru_cache
from itertools import product

sys.setrecursionlimit(10**7)

OPS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else None,
}

def tokenize(expr):
    return [token for token in re.findall(r'\d+|[()+\-*/]', expr)]

@lru_cache(maxsize=None)
def calc(tokens_tuple):
    tokens = list(tokens_tuple)
    if len(tokens) == 1:
        return {int(tokens[0])}
    results = set()
    for i, t in enumerate(tokens):
        if t in OPS:
            left = tuple(tokens[:i])
            right = tuple(tokens[i+1:])
            for a, b in product(calc(left), calc(right)):
                if t == '/' and b == 0:
                    continue
                r = OPS[t](a, b)
                if r is not None:
                    results.add(r)
    return results

def parse(tokens):
    def helper(idx):
        vals = []
        while idx < len(tokens):
            token = tokens[idx]
            if token == ')':
                return idx, tuple(vals)
            elif token == '(':
                idx, val = helper(idx + 1)
                vals.append(val)
            else:
                vals.append(token)
            idx += 1
        return idx, tuple(vals)
    _, parsed = helper(0)
    return parsed

def flatten(expr):
    # Recursively flatten parsed tokens
    if isinstance(expr, str) or isinstance(expr, int):
        return (expr,)
    flat = []
    for e in expr:
        if isinstance(e, tuple):
            flat.append(flatten(e))
        else:
            flat.append(e)
    return tuple(flat)

def main():
    for line in iter(lambda: sys.stdin.readline(), ''):
        S = line.strip()
        if S == '#':
            break
        tokens = tokenize(S)
        parsed = parse(tokens)
        fparsed = flatten(parsed)
        res = calc(fparsed)
        print(len(res))

if __name__ == '__main__':
    main()