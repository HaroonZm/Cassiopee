from collections import deque

def next_states(s):
    colors = {'r','g','b'}
    res = []
    n = len(s)
    for i in range(n-1):
        if s[i] != s[i+1]:
            # determine next color different from both
            next_color = (colors - {s[i], s[i+1]}).pop()
            new_s = s[:i] + next_color*2 + s[i+2:]
            res.append(new_s)
    return res

def bfs(start):
    if all(c == start[0] for c in start):
        return 0
    visited = set([start])
    queue = deque([(start,0)])
    while queue:
        state, t = queue.popleft()
        for nxt in next_states(state):
            if nxt not in visited:
                if all(c == nxt[0] for c in nxt):
                    return t+1
                visited.add(nxt)
                queue.append((nxt, t+1))
    return "NA"

while True:
    s = input().strip()
    if s == "0":
        break
    print(bfs(s))