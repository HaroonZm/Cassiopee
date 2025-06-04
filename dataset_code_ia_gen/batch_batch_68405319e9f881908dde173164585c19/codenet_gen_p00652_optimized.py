import sys
import bisect

input=sys.stdin.readline

while True:
    n,m,w,h,S=map(int,input().split())
    if n==0 and m==0 and w==0 and h==0 and S==0:
        break
    l=[0]*m
    r=[0]*m
    for i in range(m):
        li,ri=map(int,input().split())
        l[i]=li
        r[i]=ri
    almonds_y=[]
    almonds_x=[]
    for _ in range(n):
        x,y= map(float,input().split())
        almonds_x.append(x)
        almonds_y.append(y)
    prefix_almonds_num=[0]*(m+1)
    areas=[0]*m
    for i in range(m):
        h_strip = l[i]- (l[i-1] if i>0 else 0)
        areas[i]= h_strip * w
    prefix_areas=[0]*(m+1)
    for i in range(m):
        prefix_areas[i+1]=prefix_areas[i]+areas[i]
    almonds_in_strip=[0]*m
    # assign almonds to strips
    # each strip is between l[i-1] and l[i]
    # as l is sorted, use bisect_right on l with almond_y to find strip
    for y in almonds_y:
        idx=bisect.bisect_right(l,y)-1
        if 0<=idx<m:
            almonds_in_strip[idx]+=1
    prefix_almonds_num=[0]*(m+1)
    for i in range(m):
        prefix_almonds_num[i+1]=prefix_almonds_num[i]+almonds_in_strip[i]
    res=n+1
    j=0
    # two pointers on prefix_areas to find minimal almonds in subinterval with area>=S
    for i in range(m):
        while j<m and prefix_areas[j+1]-prefix_areas[i]<S:
            j+=1
        if j>=m:
            break
        res=min(res,prefix_almonds_num[j+1]-prefix_almonds_num[i])
    if S==0:
        res=0
    print(res if res<=n else 0)