import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
children = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    children[a].append(b)

def dfs(node):
    if not children[node]:
        return [1]
    subs = []
    max_depth = 0
    depths_lists = []
    for c in children[node]:
        dlist = dfs(c)
        depths_lists.append(dlist)
        if len(dlist) > max_depth:
            max_depth = len(dlist)
    depth_count = [1] + [0]*max_depth
    for dlist in depths_lists:
        for i in range(len(dlist)):
            depth_count[i+1] += dlist[i]
    # Remove trailing zeros
    while len(depth_count)>1 and depth_count[-1]==0:
        depth_count.pop()
    return depth_count

counts = {}
for i in range(1,N+1):
    c = dfs(i)
    t = tuple(c)
    counts[t] = counts.get(t,0)+1

res = 0
for v in counts.values():
    res += v*(v-1)//2
print(res)