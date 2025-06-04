import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
parents = []
messages = []
children = [[] for _ in range(n)]

for i in range(n):
    k = int(sys.stdin.readline())
    m = sys.stdin.readline().rstrip('\n')
    parents.append(k)
    messages.append(m)
    if k > 0:
        children[k-1].append(i)

def dfs(u, depth):
    print('.' * depth + messages[u])
    for v in children[u]:
        dfs(v, depth + 1)

dfs(0, 0)