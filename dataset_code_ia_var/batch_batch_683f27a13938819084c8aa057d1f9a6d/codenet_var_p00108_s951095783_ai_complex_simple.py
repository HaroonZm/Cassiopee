from functools import reduce
from itertools import groupby, count, takewhile, tee, starmap, repeat, islice

def stabilized_transform(seq):
    def f(s):
        return list(starmap(lambda e, l: l.count(e), enumerate(repeat(s, len(s))), list(enumerate(s))))
    history = [seq]
    def step(s):
        ns = [s.count(e) for e in s]
        return ns
    for i in count():
        next_s = step(history[-1])
        if next_s == history[-1]:
            return i, next_s
        history.append(next_s)

for _ in iter(int, 1):
    n = int(input())
    if not n:
        break
    s = list(map(int, input().split()))
    ans, res = stabilized_transform(s)
    print(ans)
    print(*res)