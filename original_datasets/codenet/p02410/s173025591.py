n,m =  map(int,input().split())
a = [[] for i in range(n)]

for i in range(n):
    a[i] = list(map(int,input().split()))

b = [[0]*1 for i in range(m)]

for i in range(m):
    b[i] = int(input())

for row in range(n):
    ans = 0
    for col in range(m):
        ans += a[row][col]*b[col]
    print(ans)