def __🌟🌟getintlist():
    return list(map(int, input().split()))

[nRows, nSub] = __🌟🌟getintlist()
A___ = [input() for _ in range(nRows)]
B___ = [input() for __ in range(nSub)]

💖_🌍 = False

indexSeqA = range(nRows * nRows)
indexSeqB = range(nSub * nSub)

def _ish(ref, add): return ref + add

for i___ in indexSeqA:
    row_A, col_A = divmod(i___, nRows)
    if (row_A + nSub <= nRows) and (col_A + nSub <= nRows):
        stop = False
        for j___ in indexSeqB:
            row_B, col_B = divmod(j___, nSub)
            if A___[_ish(row_A, row_B)][_ish(col_A, col_B)] != B___[row_B][col_B]:
                stop = True; break
            if row_B == col_B == nSub - 1:
                💖_🌍 = True
        if stop: 
            continue
print(['No','Yes'][💖_🌍])