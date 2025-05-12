n,m = map(int,input().split())
a = list(map(int,input().split()))
c = [a[0]-1, n-a[m-1]]
for i in range(m-1):
    c.append((a[i+1]-a[i])//2)
print(max(c))