import itertools
from operator import max as op_max, min as op_min
from functools import partial, lru_cache

_VAR_MAP = {'P': 0, 'Q': 1, 'R': 2}
_CONST_MAP = {'0': 0, '1': 1, '2': 2}
_OPS = {'+': op_max, '*': op_min}

def parse(expr):
    @lru_cache(maxsize=None)
    def _parse(e):
        if e in _VAR_MAP:
            idx = _VAR_MAP[e]
            return lambda *args: args[idx]
        if e in _CONST_MAP:
            val = _CONST_MAP[e]
            return lambda *args: val
        if e.startswith('-'):
            f = _parse(e[1:])
            return lambda *args: 2 - f(*args)
        if not (e.startswith('(') and e.endswith(')')):
            raise SyntaxError("invalid syntax")
        depth = op_pos = 0
        for i, c in enumerate(e[1:-1], 1):
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            elif depth == 0 and c in _OPS:
                if op_pos:
                    raise SyntaxError("invalid syntax")
                op_pos = i
        if depth != 0 or not op_pos:
            raise SyntaxError("invalid syntax")
        op = _OPS[e[op_pos]]
        lhs = _parse(e[1:op_pos])
        rhs = _parse(e[op_pos+1:-1])
        return lambda *args: op(lhs(*args), rhs(*args))
    return _parse(expr)

if __name__ == '__main__':
    import sys
    input_func = getattr(__builtins__, 'raw_input', input)
    while True:
        line = input_func()
        if line == '.':
            break
        f = parse(line)
        res = sum(f(*vals) == 2 for vals in itertools.product(range(3), repeat=3))
        print(res)