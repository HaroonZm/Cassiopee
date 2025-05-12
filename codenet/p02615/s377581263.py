n = int(input())
a = [int(i) for i in input().split()]

a.sort(reverse=True)
ans = a[0]

tmp = n-2

for i in range(n):
    if tmp == 0:
        break
    if tmp >= 2:
        ans += a[i+1]*2
        tmp -= 2
    elif tmp == 1:
        ans += a[i+1]
        tmp -= 1
    #print(ans,tmp)
        
print(ans)