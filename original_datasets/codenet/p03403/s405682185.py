n = int(input())
a = list(map(int,input().split()))
a.append(0)
a.insert(0,0)
b = 0
for i in range(n+1):
    b += abs(a[i]-a[i+1])
for i in range(1,n+1):
    c = b + abs(a[i-1]-a[i+1]) - abs(a[i]-a[i+1])-abs(a[i]-a[i-1])
    print(c)