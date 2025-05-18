while 1:
    n = float(input())
    if n<0:break
    m=n-int(n)
    a=bin(int(n))[2:].zfill(8)+'.'
    for _ in range(4):
        m*=2
        if m>=1:
            a+='1'
            m-=1
        else: a+='0'
    print('NA' if m>1e-10 or 13<len(a) else a)