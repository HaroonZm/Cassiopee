while True:
    h,w=map(int,input().split())
    if h==0 and w==0: break
    board=[input() for _ in range(h)]
    s=input()
    pos={}
    for i in range(h):
        for j in range(w):
            c=board[i][j]
            if c!='_':
                pos[c]=(i,j)
    ci,cj=0,0
    res=0
    for c in s:
        ni,nj=pos[c]
        res+=abs(ni-ci)+abs(nj-cj)+1
        ci,cj=ni,nj
    print(res)