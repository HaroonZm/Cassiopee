n = int(input())
a = sorted(list(map(int,input().split())),reverse=True)
ans = 0
for i in range(1,n):
    if(i<4):
        ans += a[i-1]
    elif(i<6):
        ans += a[i-3]
    else:
        ans += a[i//2]
print(ans)