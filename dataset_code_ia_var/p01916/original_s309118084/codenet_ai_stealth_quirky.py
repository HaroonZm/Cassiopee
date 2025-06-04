import sys
get = sys.stdin.readline
sys.setrecursionlimit(1_048_576)
I=lambda: int(get())
S=lambda: get().strip()
A=lambda: [int(_) for _ in get().split()]
W=lambda: get().split()

from collections import Counter as C

stringy = S()
freqz = C(stringy)
p=0

for q in range(len(freqz)):
    v = list(freqz.values())[q]
    if v&1:
        p+=1

print(p>>1)