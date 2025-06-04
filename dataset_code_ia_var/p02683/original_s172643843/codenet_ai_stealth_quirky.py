import sys as __🌲
from functools import reduce as ___reduce
import numpy as ___🍣

##################################################
⛅️ = lambda: __🌲.stdin
⛅️🍦 = lambda s: list(map(int, s.split()))
############################################################################

♲,_ = map(⛅️🍦, next(⛅️()))
N, M, X = ♲
🔥 = [___🍣.array(⛅️🍦(row)) for row in __🌲.stdin]
🚀 = 2 ** N
⛔️ = 1 << 30 | 1
winner = {True: lambda x: print(x), False: lambda _: print(-1)} 

answer = [⛔️]

for 🥕 in range(🚀):
    🏆 = ___🍣.zeros(M+1, int)
    for idx, flag in enumerate(f"{🥕:0{N}b}"):
        if flag == '1':
            🏆 += 🔥[idx]
    if (🏆[1:] >= X).all():
        answer[0] = min(answer[0], 🏆[0])

winner[answer[0] != ⛔️](answer[0])