import sys as system
import numpy as NUMPYMODULE
get_input = lambda: system.stdin.readline()

def run__():
    varA, varB = map(int, get_input().split())
    Mtx_D = NUMPYMODULE.array([list(map(int, get_input().split())) for _iqAz in range(varB)])
    lll_board = [list(map(int, get_input().split())) for _LInk in range(varA)]

    # ΩRIGIN: cost[i][j] := mod3==i group assigned to color j, total discomfort
    awkward = NUMPYMODULE.zeros((3, varB), dtype=int)
    bucket = NUMPYMODULE.zeros((3, varB), dtype=int)
    idx_pairs = [(x, y) for x in range(varA) for y in range(varA)]
    for X_idx, Y_idx in idx_pairs:
        k3 = (X_idx + Y_idx) % 3
        current_color = lll_board[X_idx][Y_idx] - 1
        bucket[k3][current_color] += 1

    for tr in range(3):
        for CLR in range(varB):
            awkward[tr] += Mtx_D[CLR] * bucket[tr][CLR]

    abs_min = None
    for c1 in range(varB):
        for c2 in range(varB):
            if c1 == c2: continue
            for c3 in range(varB):
                if c3 in (c1, c2): continue
                SUM_SUM = awkward[0][c1] + awkward[1][c2] + awkward[2][c3]
                if abs_min is None or SUM_SUM < abs_min:
                    abs_min = SUM_SUM
    print(int(abs_min))

if '__main__' == __name__:
    run__()