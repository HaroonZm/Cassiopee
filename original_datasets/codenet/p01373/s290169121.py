iipt=lambda:int(input())
miipt=lambda: list(map(int, input().split()))
while True:
    w,h,n=miipt()
    if w==h==n==0: break
    s=[miipt() for i in range(2*n)]
    right=[0,h]
    for i, (x1,y1) in enumerate(s):
        if x1<w:
            t=y1*w/(w-x1)
            if 0<=t<=h:
                right.append(t)
            t = h-(h-y1)*w/(w-x1)
            if 0<=t<=h:
                right.append(t)
        for x2,y2 in s[:i]:
            if x1!=x2:
                t = y2-(y2-y1)/(x2-x1)*x2
                if 0<=t<=h:
                    right.append(t)

    right.sort()
    ans=0
    INF=1e16
    EPS=1e-11
    #print(right)
    for y1,y2 in zip(right, right[1:]):
        if abs(y2-y1)<1e-11:
            continue
        y=(y1+y2)/2
        a,b = sorted([max(0,min(h,y+(y_-y)/(x_+EPS)*w))  for x_, y_ in s])[n-1:n+1]
        #print(y1,y2,[(y_-y)/x_ if x_ else INF if y_>y else -INF for x_, y_ in s])
        #A=max(0,min(h,y+a*w))
        #B=max(0,min(h,y+b*w))
        ans+=(y2-y1)*(b-a)
        #print((y2-y1),(B-A),(a,A),(b,B))

    print("{:0.11f}".format(ans/h/h))