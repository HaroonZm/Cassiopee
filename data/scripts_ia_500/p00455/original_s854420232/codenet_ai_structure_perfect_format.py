t=[list(map(int,input().split())) for _ in range(3)]
for i in range(3):
    r=t[i]
    if r[5]-r[2]>=0:
        s=r[5]-r[2]
    else:
        s=60-(r[2]-r[5])
        r[4]-=1
    if r[4]-r[1]>=0:
        m=r[4]-r[1]
    else:
        m=60-(r[1]-r[4])
        r[3]-=1
    h=r[3]-r[0]
    print(h,m,s)