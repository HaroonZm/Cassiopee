n,l=map(int,input().split())
taste=10000
for i in range(1,n+1):
    if abs(taste)>abs(l+i-1):
        taste=l+i-1
        
print(n*l+(n*(n+1)//2)-n-taste)