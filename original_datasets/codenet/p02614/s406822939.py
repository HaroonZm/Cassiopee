from itertools import *
import numpy as np
H,W,K = map(int,input().split())
C = [list(input()) for h in range(H)]
D = np.zeros((H,W),dtype=np.int)
a = 0

for h in range(H):
  for w in range(W):
    if C[h][w]=="#":
      D[h][w]=1

T = np.sum(D)

for h in range(1+H):
  for I in combinations(range(H),h):
    for w in range(1+W):
      for J in combinations(range(W),w):
        S = 0
        
        for i in I:
          for w in range(W):
            S+=D[i][w]
        for j in J:
          for h in range(H):
            S+=D[h][j]
        for i in I:
          for j in J:
            S-=D[i][j]
        
        if K==T-S:
          a+=1

print(a)