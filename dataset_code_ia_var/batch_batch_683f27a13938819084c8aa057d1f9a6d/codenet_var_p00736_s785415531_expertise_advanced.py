import operator
import re
from functools import lru_cache
from itertools import product

def parse_parenthesis(formula):
    count = 0
    # Find top-level operator and split operands efficiently
    for i, char in enumerate(formula):
        if char == '(': count += 1
        elif char == ')': count -= 1
        elif count == 1 and char in '+*':
            return formula[1:i], char, formula[i+1:-1]
    raise ValueError("Invalid formula structure")

OR_MAP = {
    ('0', '0'): '0', ('0', '1'): '1', ('0', '2'): '2',
    ('1', '0'): '1', ('1', '1'): '1', ('1', '2'): '2',
    ('2', '0'): '2', ('2', '1'): '2', ('2', '2'): '2'
}
AND_MAP = {
    ('0', '0'): '0', ('0', '1'): '0', ('0', '2'): '0',
    ('1', '0'): '0', ('1', '1'): '1', ('1', '2'): '2',
    ('2', '0'): '0', ('2', '1'): '2', ('2', '2'): '2'
}
NEG_MAP = {'0': '2', '1': '1', '2': '0'}

def eval_or(a, b): return OR_MAP[a, b]
def eval_and(a, b): return AND_MAP[a, b]
def eval_neg(a): return NEG_MAP[a]

@lru_cache(maxsize=None)
def evaluate(formula, p, q, r):
    if formula in {'0', '1', '2'}:
        return formula
    if formula in {'P', 'Q', 'R'}:
        return {'P': p, 'Q': q, 'R': r}[formula]
    if formula[0] == '(':
        a, op, b = parse_parenthesis(formula)
        func = eval_or if op == '+' else eval_and
        return func(evaluate(a, p, q, r), evaluate(b, p, q, r))
    if formula[0] == '-':
        return eval_neg(evaluate(formula[1:], p, q, r))
    raise ValueError(f"Unexpected formula: {formula}")

if __name__ == "__main__":
    try:
        while True:
            formula = input().strip()
            if formula == '.':
                break
            print(sum(
                evaluate(formula, str(p), str(q), str(r)) == '2'
                for p, q, r in product(range(3), repeat=3)
            ))
    except EOFError:
        pass