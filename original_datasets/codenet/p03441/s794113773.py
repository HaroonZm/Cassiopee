import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

s = -1
for n in range(N):
    if len(graph[n]) > 2:
        s = n
        break

checked = [False]*N

def dfs2(s):
    ans = 0
    S = [0]*N
    T = [0]*N
    # Req = [True]*N
    Ind = [0]*N
    stack = [s]
    while stack:
        p = stack[-1]
        if Ind[p] == len(graph[p]):
            ans += max(T[p] - S[p] - 1, 0)
            stack.pop()
            if stack:
                par = stack[-1]
                T[par] += 1
                if S[p] > 0 or T[p] > 1:
                    S[par] += 1
        elif len(stack) > 1 and stack[-2] == graph[p][Ind[p]]:
            Ind[p] += 1
        else:
            stack.append(graph[p][Ind[p]])
            Ind[p] += 1
    return ans

if s == -1:
    ans = 1
else:
    ans = dfs2(s)

print(ans)