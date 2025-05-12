import sys
sys.setrecursionlimit(1010)

N = int(input())
src = []
for i in range(N):
    k = int(input())
    s = input()
    src.append((s,[]))
    if i == 0: continue
    src[k-1][1].append(i)

def dfs(i,depth):
    s,ch = src[i]
    print('.'*depth + s)
    for c in ch:
        dfs(c,depth+1)

dfs(0,0)