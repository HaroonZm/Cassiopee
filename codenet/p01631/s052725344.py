import sys
from collections import defaultdict,deque
def dfs(d,f,y,x):
    if d == len(w):
        m[k] += 1
    else:
        for dy,dx in move:
            y_ = y+dy
            x_ = x+dx
            if 0 <= y_ < 4 and 0 <= x_ < 4:
                if f[y_][x_]:
                    if s[y_][x_] == w[d]:
                        f[y_][x_] = 0
                        dfs(d+1,f,y_,x_)
                        f[y_][x_]= 1
move = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
n = int(sys.stdin.readline())
word = [sys.stdin.readline().split() for i in range(n)]
s = [sys.stdin.readline()[:-1] for i in range(4)]
W = int(sys.stdin.readline())
m = [0]*n
q = deque()
k = 0
for w,p in word:
    for b in range(4):
        for a in range(4):
            if s[b][a] == w[0]:
                f = [[1]*4 for i in range(4)]
                f[b][a] = 0
                dfs(1,f,b,a)
    k += 1

w = [len(word[i][0]) for i in range(n)]
v = [int(word[i][1]) for i in range(n)]
dp = [0]*(W+1)
deq = [0]*(W+1)
deqv = [0]*(W+1)
for i in range(n):
    for a in range(w[i]):
        s = 0
        t = 0
        j = 0
        while j*w[i]+a <= W:
            val = dp[j*w[i]+a]-j*v[i]
            while s < t and deqv[t-1] <= val:t -= 1
            deq[t] = j
            deqv[t] = val
            t += 1
            dp[j*w[i]+a] = deqv[s]+j*v[i]
            if deq[s] == j-m[i]:
                s += 1
            j += 1
print(dp[W])