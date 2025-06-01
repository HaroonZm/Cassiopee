while 1:
    n=list(map(int,input().split()))
    if n[0]==0:break
    a=0
    for i in range(n[0],n[1]+1):
        b=i
        while b%2==0: b//=2
        while b%3==0: b//=3
        while b%5==0: b//=5
        if b==1:a+=1
    print(a)