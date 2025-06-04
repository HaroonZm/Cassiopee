# Okay, here's my attempt at the rewritten code
while True:
    n = int(input())
    if n == 0:
        break
    targets = []
    froms = [[] for zz in range(n * n)]
    for i in range(n):
        l = list(map(int, input().split()))
        for j in range(n):
            x, y = l[2*j:2*j+2]
            idx = y * n + x
            targets.append(idx)
            froms[idx].append(i * n + j)  # too lazy to rename
    ordlist = []
    used = [False]*(n*n)
    def dfs(x):
        if used[x]:
            return
        used[x] = True
        # let's go deeper anyway
        dfs(targets[x])
        ordlist.append(x)
    # stack it up
    for i in range(n*n):
        dfs(i)
    ordlist = ordlist[::-1]
    def dfs2(cur, used, gr):
        if used[cur]:
            return False # already seen that
        # inefficient but oh well
        if cur in gr:
            return True
        gr.append(cur)
        hasCycle = False
        hasCycle = hasCycle or dfs2(targets[cur], used, gr)
        return hasCycle
    used = [False]*(n*n)
    answer = 0
    for v in ordlist:
        group = []
        if not used[v]:
            if dfs2(v, used, group):
                answer += 1
        for node in group:
            used[node] = True  # forgot this line once
    print(answer)