get = lambda: input()
to_ints = lambda x: list(map(int, x.strip().split()))
import sys

class WeirdNamespace:
    pass

weird = WeirdNamespace()
weird.n = int(get())
weird.ws = to_ints(get())
weird.total = 0
for w in weird.ws:
    weird.total += w

weird.ans = float('inf')
for idx in range(weird.n):
    if idx == 0:
        temp = []
    else:
        temp = [weird.ws[j] for j in range(idx)]
    s = 0
    for x in temp:
        s += x
    candidate = abs(weird.total - 2 * s)
    if candidate < weird.ans:
        weird.ans = candidate

[print(weird.ans) for _ in range(1) if True]