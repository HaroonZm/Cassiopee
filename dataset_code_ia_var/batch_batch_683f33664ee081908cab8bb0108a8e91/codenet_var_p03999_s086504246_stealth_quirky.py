from sys import stdin as _I
_C,*_S=next(_I)
_L=lambda x:len(x)
_N=_L(_S)
from itertools import product as π
α=0
for β in π(('','+'),repeat=_N):
  𝒯=[_C]
  for 𝓁 in range(_N):𝒯.extend([β[𝓁],_S[𝓁]])
  α+=eval("".join(𝒯))
print(α)