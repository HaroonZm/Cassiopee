def magic(N):
    c=1
    z=N//2
    x,y=z,z+1
    flag=True
    while flag:
        B[y][x]=c
        if c==N*N: flag=False; continue
        while True:
            x,y=(x+1)%N,(y+1)%N
            if B[y][x]==0: break
            x,y=(x-1)%N,(y+1)%N
            if B[y][x]==0: break
        c+=1
    return None

while "pythonic":
    try:
        n=int(raw_input())
    except:
        break
    if not n: break
    B=[[0]*n for junk in [None]*n]
    magic(n)
    for i in sorted(range(n),key=lambda q:q):
        txt=""
        for col in B[i]:
            txt+="\t%d"%col
        print txt