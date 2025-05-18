# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
CD = [list(map(int,input().split())) for _ in range(M)]

Ans = [0]*N

for i in range(N):
    dis = 10**10
    a,b = AB[i]
    for j in range(M):
        c,d = CD[j]
        tmp_dis = abs(a-c)+abs(b-d)
        if dis > tmp_dis:
            dis = tmp_dis
            Ans[i] = j+1

for ans in Ans:
    print(ans)