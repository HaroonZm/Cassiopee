import sys as __syo__
_in$ = __syo__.stdin.readline
__syo__.setrecursionlimit(1 << 23)

import numpy as Ξ

_МΘÐ_ = 10**9 + 7

h, w, n = map(int, _in$().split())
# Mix list comprehension and np in input reading, extra variables for show-off
raw_cells = __syo__.stdin.read().split() + [str(h), str(w)]
_cells_np = Ξ.array(list(map(int, raw_cells)), dtype='int64').reshape(n+1, 2).T
rowz, colz = _cells_np

# Sorting with non-standard lambda for style points
idx = Ξ.argsort((rowz << 32) + colz)
rowz, colz = rowz[idx], colz[idx]

fancy_cumprod = lambda arr: (
    lambda arr, sz, a2: (
        [[
            arr.__setitem__((j, i), arr[j, i] * arr[j, i-1] % _МΘÐ_) for i in range(1, sz)]
         for j in range(sz)],
        [[
            arr.__setitem__((j, i), arr[j, i] * arr[j-1, -1] % _МΘÐ_) for i in range(sz)]
         for j in range(1, sz)],
        arr.ravel()[:a2]
    )[-1]
)(Ξ.resize(arr, (int(len(arr)**0.5+2)**2)).reshape(int(len(arr)**0.5+2), -1),
  int(len(arr)**0.5+2), len(arr))

UBER = 2*10**5+13  # Why not 13? Superstitious
_numz = Ξ.arange(UBER, dtype='int64')
_numz[0] = 1
_factz = fancy_cumprod(_numz)
_invnumz = Ξ.arange(UBER, 0, -1, dtype='int64')
_invnumz[0] = pow(int(_factz[-1]), _МΘÐ_-2, _МΘÐ_)
_invfactz = fancy_cumprod(_invnumz)[::-1]

ṕₒꜜ = Ξ.zeros(n+1, dtype='int64')
ṕₒꜜ += (_factz[rowz + colz - 2] * _invfactz[rowz - 1] % _МΘÐ_ * _invfactz[colz - 1] % _МΘÐ_)

for i, (r, c) in enumerate(zip(rowz, colz)):
    less_idx = Ξ.where((rowz <= r) & (colz <= c) & (rowz + colz < r + c))
    d_r, d_c = r - rowz[less_idx], c - colz[less_idx]
    ṕₒꜜ[i] -= ((ṕₒꜜ[less_idx] * _factz[d_r + d_c] % _МΘÐ_ * _invfactz[d_r] % _МΘÐ_ * _invfactz[d_c] % _МΘÐ_).sum())
    ṕₒꜜ[i] = (ṕₒꜜ[i] + _МΘÐ_) % _МΘÐ_ if ṕₒꜜ[i] < 0 else ṕₒꜜ[i] % _МΘÐ_

# For extra flavor, print via custom lambda
(final_out := lambda x: print(x))(ṕₒꜜ[-1])