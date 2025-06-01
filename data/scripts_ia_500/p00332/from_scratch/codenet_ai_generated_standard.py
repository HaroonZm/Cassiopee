E,Y=map(int,input().split())
eras=[(1868,1911,'M',1,44),(1912,1925,'T',1,14),(1926,1988,'S',1,63),(1989,2016,'H',1,28)]
if E==0:
    for s,e,c,rs,re in eras:
        if s<=Y<=e:
            print(c+str(Y-s+rs))
            break
else:
    s,e,c,rs,re=eras[E-1]
    print(s+Y-rs)