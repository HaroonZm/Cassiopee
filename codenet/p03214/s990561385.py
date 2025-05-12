n = int(input())
a = list(map(int,input().split()))
ave = sum(a)/n

ans = 0
sw = float("Inf")
for i in range(n):
    if abs(ave-a[i]) < sw:
        ans = i
        sw = abs(ave-a[i])
        
print(ans)