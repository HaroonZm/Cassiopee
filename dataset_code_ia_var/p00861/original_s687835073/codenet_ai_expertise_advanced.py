import re
from collections import defaultdict
import operator
from functools import partial

init_pat = re.compile(r"([^\[]+)\[([^\]=]+)\]$")
assign_pat = re.compile(r"([^\[]+)\[([^\]=]+)\]=(.+)$")

def optimized_eval(dic, sz):
    def _eval(expr):
        try:
            if (m := init_pat.fullmatch(expr)):
                name, idx_expr = m.groups()
                idx = _eval(idx_expr)
                return dic[name][idx]
            return eval(expr, {}, {})
        except Exception:
            return -1
    return _eval

def main():
    import sys
    input_func = (lambda: sys.stdin.readline().rstrip()) if hasattr(sys.stdin, "readline") else (lambda: input())
    while True:
        dic = defaultdict(dict)
        sz = {}
        ans = 0
        idx = 0
        _eval = optimized_eval(dic, sz)
        while True:
            s = input_func()
            if s == '.':
                break
            idx += 1
            if (m := init_pat.fullmatch(s)):
                name, expr = m.groups()
                val = _eval(expr)
                if val == -1 and ans == 0:
                    ans = idx
                else:
                    dic[name] = {}
                    sz[name] = val
            elif (m := assign_pat.fullmatch(s)):
                name, expr, rhs = m.groups()
                i = _eval(expr)
                v = _eval(rhs)
                if i == -1 or v == -1 or name not in dic or i < 0 or i >= sz.get(name, -1):
                    if ans == 0:
                        ans = idx
                else:
                    dic[name][i] = v
        if not dic:
            break
        print(ans)

main()