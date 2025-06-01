n=int(input())
a=list(map(int,input().split()))
a.sort()
max_val=float('-inf')
# Pour éviter division par 0, on teste les différences non nulles
for i in range(n):
    for j in range(n):
        if i==j: continue
        denom=a[i]-a[j]
        if denom==0: continue
        for x in range(n):
            if x==i or x==j: continue
            for y in range(x+1,n):
                if y==i or y==j: continue
                val=(a[x]+a[y])/denom
                if val>max_val:
                    max_val=val
print(f"{max_val:.6f}")