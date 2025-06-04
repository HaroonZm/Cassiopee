from itertools import permutations, product
import sys

ops = ['+', '-', '*']

def eval_expr(expr):
    try:
        return eval(expr)
    except:
        return None

def generate_exprs(nums):
    # Generate all valid expressions with three operators and four numbers with parentheses
    a, b, c, d = nums
    op_combinations = product(ops, repeat=3)
    # Different ways to parenthesize four numbers with three operators (only 5 ways)
    patterns = [
        '(({} {} {}) {} {}) {} {}',
        '({} {} ({} {} {})) {} {}',
        '{} {} (({} {} {}) {} {})',
        '{} {} ({} {} ({} {} {}))',
        '({} {} {}) {} ({} {} {})',
    ]
    for ops_choice in op_combinations:
        for pat in patterns:
            expr = pat.format(a, ops_choice[0], b, ops_choice[1], c, ops_choice[2], d)
            if len(expr) > 1024:
                continue
            val = eval_expr(expr)
            if val == 10:
                return expr
    return None

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        parts = line.strip().split()
        if len(parts) != 4:
            continue
        nums = tuple(map(int, parts))
        if nums == (0,0,0,0):
            break
        found = None
        for perm in permutations(nums):
            res = generate_exprs(perm)
            if res is not None:
                found = res
                break
        if found:
            print(found)
        else:
            print(0)

if __name__ == "__main__":
    main()