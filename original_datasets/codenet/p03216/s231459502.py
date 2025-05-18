import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

N = int(readline())
S = np.frombuffer(readline().rstrip(),'S1')
Q = int(readline())
query = map(int,read().split())

isD = S == b'D'
isM = S == b'M'
isC = S == b'C'

cumD = isD.cumsum(dtype=np.int64)
cumM = isM.cumsum(dtype=np.int64)

def F(K):
    """
    ・Cごとに数える。
    ・そのためには(i-K,i] 内のDMの個数を調べる（負インデックスには関係ない文字があると思っておく）
    ・区間内のDの個数、Mの個数が取得できれば、差分が取得できるので最後に累積和
    """
    # (i-K,i]内のDの個数、Mの個数
    D = cumD.copy(); D[K:] -= cumD[:-K]
    M = cumM.copy(); M[K:] -= cumM[:-K]
    # 最後がMのとき、Dの個数分増える
    DM = isM * D
    # 左端のDを捨てるとき、Mの個数分減る
    DM[K:] -= isD[:-K] * M[K-1:-1]
    np.cumsum(DM,out=DM)
    # Cごとに集計
    return DM[isC].sum()

print('\n'.join(str(F(K)) for K in query))