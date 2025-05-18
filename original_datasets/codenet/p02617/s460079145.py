N=int(input())
G = [[] for i in range(N)]
ans = 0
for i in range(1,N+1):
    ans += (N-i+1)*(N-i+2)//2
for i in range(N-1):
    a, b = map(int, input().split())
    a, b = min(a,b),max(a,b)
    #print(a,b)
    ans -= a * (N-b+1)
print(ans)