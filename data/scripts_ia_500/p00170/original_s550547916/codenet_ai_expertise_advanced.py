from sys import stdin

def solve(placed, w1, w2):
    remain = [e for e in N if e not in placed]
    if not remain:
        a = tuple(placed)
        D1[a] = w1
        D2[a] = w2
        return
    n = len(remain)
    for e in remain:
        w = Food[e][0]
        if w2 > Food[e][1]:
            return
        solve(placed + [e], w1 + w * n, w2 + w)

for line in stdin:
    n = line.strip()
    if n == '0':
        break
    n = int(n)
    D1, D2 = {}, {}
    Name, Food = {}, {}
    N = range(n)
    for i in N:
        parts = stdin.readline().split()
        Name[i] = parts[0]
        Food[i] = list(map(int, parts[1:]))
    solve([], 0, 0)
    Index, _ = min(D1.items(), key=lambda x: x[1])
    for e in reversed(Index):
        print(Name[e])