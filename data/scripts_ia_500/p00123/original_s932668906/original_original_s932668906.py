import bisect
while 1:
    try:
        n,m=map(float,input().split())
        m500=[35.5,37.5,40,43,50,55,70]
        m1000=[71,77,83,89,105,116,148]
        r1=bisect.bisect_left(m500,n+0.001)
        r2=bisect.bisect_left(m1000,m+0.001)
        rank=["AAA","AA","A","B","C","D","E","NA"]
        print(rank[max(r1,r2)])
    except:break