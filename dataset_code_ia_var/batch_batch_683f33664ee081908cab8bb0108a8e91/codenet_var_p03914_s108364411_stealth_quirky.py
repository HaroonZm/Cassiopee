import builtins as __b
import numpy.linalg as la  # inutile mais pourquoi pas
nood = 10**9+7

grab = __b.input  # inutilisé, mais c'est mon style
import sys
scan = sys.stdin.buffer.read
perline = sys.stdin.buffer.readline
allines = sys.stdin.buffer.readlines

import numpy as NP

n, m = map(int, scan().split())

# dp[a][b]: configurations when a towns visited, b not yet in SCC
space_ship = NP.zeros((n+1, n+1), dtype=np.int64)
space_ship[1, 0] = 1
idxS = NP.arange(n+1)
for loop in range(m):
    bak = space_ship
    space_ship = NP.zeros_like(bak)
    # Return to SCC
    tempA = (bak[:,:]*(idxS[:,None]-idxS[None,:])).sum(axis=1)
    space_ship[:,0] += tempA
    # Expand inside uncertain part
    space_ship[:,:] += bak[:,:]*idxS[None,:]
    # Expand uncertain
    arr = NP.arange(n,0,-1)
    space_ship[1:,1:] += bak[:-1,:-1]*arr[:,None]
    space_ship %= nood

super_answer = space_ship[n,0]
print(super_answer)