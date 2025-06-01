from sys import stdin
from operator import itemgetter
from functools import reduce
from collections import deque

def solve():
    src = map(str.strip, iter(stdin.readline, ''))
    n = int(next(src))
    grid = tuple(tuple(map(int, row.split())) for row in src)
    prefix_rows = tuple(((0,)+tuple(reduce(lambda a,b: a+[a[-1]+b], row, [0])[1:])) for row in grid)
    prefix_cols_tuples = tuple(zip(*grid))
    prefix_cols = tuple(((0,)+tuple(reduce(lambda a,b: a+[a[-1]+b], col, [0])[1:])) for col in prefix_cols_tuples)
    prefix_cols_trans = tuple(zip(*prefix_cols))

    ans = -float('inf')
    for i, (row, pre_row, pre_col, pre_col0) in enumerate(zip(grid, prefix_rows, prefix_cols_trans, prefix_cols[0])):
        val_r_i = pre_row[i]
        for j, (r2, prr2, pcj, pc0_j) in enumerate(zip(row[i:], pre_row[i+1:], pre_col[i+1:], pre_col0[i+1:]), start=i):
            diff = prr2 - val_r_i
            if diff > ans:
                ans = diff
            if i == j:
                continue
            col_max = pc0_j - pre_col0[i]
            it1 = zip(pcj, pre_col[i], row[1:], r2[1:])
            def fold_col(acc, tpl):
                cm, best = acc
                acj, aci, g_i, g_j = tpl
                col_val = acj - aci
                cand = max(cm+g_i+g_j, col_val, cm if cm>0 else float('-inf'))
                b_new = max(best, (col_max + col_val if col_max>0 else col_val), cand)
                cm_new = cand if cand > col_val else col_val
                return (cm_new, b_new)
            _, best_local = reduce(fold_col, it1, (col_max, ans))
            ans = max(ans, best_local)
    print(ans)

solve()