from itertools import product
import sys

sys.setrecursionlimit(10**6)

ops_replace = {
    "-0": "2",
    "-1": "1",
    "-2": "0"
}

def eval_expr(expr, subs):
    s = expr.translate(subs)
    while len(s) > 1:
        for k, v in ops_replace.items():
            s = s.replace(k, v)
        for a, b in product("012", repeat=2):
            s = s.replace(f"({a}*{b})", str(min(int(a), int(b))))
            s = s.replace(f"({a}+{b})", str(max(int(a), int(b))))
    return s

def main():
    input_fn = input if sys.version_info[0] >= 3 else raw_input
    for line in iter(input_fn, '.'):
        ans = sum(
            eval_expr(line, str.maketrans({'P': str(p), 'Q': str(q), 'R': str(r)})) == "2"
            for p, q, r in product(range(3), repeat=3)
        )
        print(ans) if sys.version_info[0] >= 3 else sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    main()