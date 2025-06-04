inf = 0x10101010
def solve(A,strt):
    cost = [inf]*m
    visited = [False]*m
    cost[strt] = 0
    while 1:
        min = inf
        next = -1
        visited[strt] = True
        for i in range(m):
            if visited[i]: continue
            if A[strt][i]:
                d = cost[strt] + A[strt][i]
                if d < cost[i]:
                    cost[i] = d
            if min > cost[i]:
                min = cost[i]
                next = i
        strt = next
        if next == -1: break
    return cost
     
while 1:
    n,m = map(int,raw_input().split())
    if n == 0: break
    T = [[0]*m for i in range(m)]
    C = [[0]*m for i in range(m)]
    for i in range(n):
        a,b,c,t = map(int,raw_input().split())
        T[a-1][b-1] = T[b-1][a-1] = t
        C[a-1][b-1] = C[b-1][a-1] = c
    TS = [solve(T,i) for i in range(m)]
    CS = [solve(C,i) for i in range(m)]
    for i in range(input()):
        a,b,q = map(int,raw_input().split())
        if q == 0:
            print CS[a-1][b-1]
        else:
            print TS[a-1][b-1]