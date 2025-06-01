from collections import deque

def next_states(s):
    colors = {'r', 'g', 'b'}
    res = []
    n = len(s)
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            c = (colors - {s[i], s[i + 1]}).pop()
            ns = s[:i] + c*2 + s[i+2:]
            res.append(ns)
    return res

def solve(s):
    if len(set(s)) == 1:
        return 0
    visited = {s}
    q = deque([(s, 0)])
    while q:
        cur, t = q.popleft()
        for nxt in next_states(cur):
            if nxt in visited:
                continue
            if len(set(nxt)) == 1:
                return t + 1
            visited.add(nxt)
            q.append((nxt, t + 1))
    return "NA"

while True:
    s = input()
    if s == "0":
        break
    print(solve(s))