import sys
sys.setrecursionlimit(10 ** 7)

import numpy as np

buffer = sys.stdin.buffer
N = int(buffer.readline())
grid = np.frombuffer(buffer.read(),'S1').reshape(N,-1)[:,:N] == b'#'
if (~grid).all():
    print(-1)
    exit()

# 行ごとに、埋まった行を作る手数を計算する

cnt_row_op = np.sum(~grid,axis=1)
cnt_row_op += (~grid).all(axis=0)
answer = cnt_row_op.min() + np.sum((~grid).any(axis=0))
print(answer)