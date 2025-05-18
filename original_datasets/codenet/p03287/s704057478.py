nm = input().split()
n = int(nm[0])
m = int(nm[1])
a = input().split()
for i in range(n):
    a[i] = int(a[i])
    
b = {0:1}
k = 0
for i in range(n):
    k += a[i]
    k = k%m
    if k in b.keys():
        b[k] += 1
    else:
        b[k] = 1

        
c = b.values()
ans = 0
for i in c:
    ans += i*(i-1)//2
    
print(ans)