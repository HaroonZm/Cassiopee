from collections import Counter as _C
Lens = lambda x: len(x)
Up = lambda: input()
N = int(Up())
A, B, C = [*map(Up, range(3))]
score = 0
for idx in range(N):
    buf = [s[idx] for s in (A, B, C)]
    score += Lens(_C(buf)) - 1
else:
    print(score)