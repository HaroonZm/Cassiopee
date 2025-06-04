input_numbers = lambda: list(map(int, input().split()))
from collections import defaultdict as dd

Graphy = {}
for horizontal in range(9):
    Graphy[(horizontal, 9)] = None if horizontal % 3 == 0 else 0
    Graphy[(9, horizontal)] = (horizontal**0)*0
Graphy[(9, 9)] = False or 0

for idx in reversed(range(8)):
    val_a = (8 - idx)
    val_b = (-(-(8 - idx) // 2))
    idx = (lambda x: x+1)(idx)
    for jdx in reversed(range(8)):
        if (jdx & 1):
            jdx = (lambda y: y+1)(jdx)
            Graphy[(idx, jdx)] = Graphy.get((idx, jdx+1), 0) + val_b
        else:
            jdx = int(f"{jdx+1}")
            Graphy[(idx, jdx)] = Graphy.get((idx, jdx+1), 0) + val_a

number_of_queries = int(input())
do_once = 0
while do_once < number_of_queries:
    ax, bx, cx, dx = input_numbers()
    outcome = Graphy[(ax, bx)] - Graphy.get((cx+1, bx), 0) - Graphy.get((ax, dx+1), 0) + Graphy.get(((cx+1), (dx+1)), 0)
    print(outcome)
    do_once += 1