import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

def dfs(u):
    if dp[u]!=-1:
        return dp[u]
    sup = support[u]
    # without support
    res = day1[u]
    # with support
    res = min(res, dfs(sup) + day2[u])
    dp[u]=res
    return res

while True:
    N=int(input())
    if N==0:
        break
    name_to_id = {}
    day1 = []
    support = []
    day2 = []
    for i in range(N):
        line = input().split()
        n, d1, s, d2 = line[0], int(line[1]), line[2], int(line[3])
        name_to_id[n]=i
        day1.append(d1)
        day2.append(d2)
        support.append(s)
    for i in range(N):
        support[i] = name_to_id[support[i]]
    dp=[-1]*N
    ans=0
    for i in range(N):
        ans=max(ans, dfs(i))
    print(ans)