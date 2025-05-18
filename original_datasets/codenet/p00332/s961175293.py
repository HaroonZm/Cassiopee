e,y=map(int,input().split())
ei=[0,1867,1911,1925,1988]
if e==0:
    if y>1988:
        print(f'H{y-1988}')
    elif y>1925:
        print(f'S{y-1925}')
    elif y>1911:
        print(f'T{y-1911}')
    else:
        print(f'M{y-1867}')
else:
    print(ei[e]+y)