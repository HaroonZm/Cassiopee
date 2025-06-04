from itertools import product
from operator import add, sub
import sys

S = input()
ops = [('+', add), ('-', sub)]
digits = list(map(int, S))

for opseq in product(ops, repeat=3):
    expr = str(digits[0])
    val = digits[0]
    for i, (sym, fn) in enumerate(opseq):
        val = fn(val, digits[i+1])
        expr += sym + str(digits[i+1])
    if val == 7:
        print(f"{expr}=7")
        sys.exit()