import sys
sys.setrecursionlimit(5000)

def dfs(x):
    global ng, parity
    for v in adj[x]:
        if parity[v] == parity[x]:
            ng = True
            return
        elif parity[v] < 0:
            parity[v] = 1^parity[x]
            dfs(v)
    return

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    adj = [[] for _ in range(n)]
    parity = [-1 for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    ng = False
    parity[0] = 0
    dfs(0)
    if ng:
        print(0)
        continue
    ans = []
    zero = parity.count(0)
    if zero%2 == 0:
        ans.append(zero//2)
    if (n-zero)%2 == 0 and zero*2 != n:
        ans.append((n-zero)//2)
    ans.sort()
    print(len(ans))
    if ans:
        print(*ans, sep="\n")