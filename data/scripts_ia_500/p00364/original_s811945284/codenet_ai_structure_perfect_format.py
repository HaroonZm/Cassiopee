n,x=map(int,input().split())
max_slope=0.0
for i in range(n):
    xi,hi=map(float,input().split())
    slope=hi/xi
    if slope>max_slope:
        max_slope=slope
print(x*max_slope)