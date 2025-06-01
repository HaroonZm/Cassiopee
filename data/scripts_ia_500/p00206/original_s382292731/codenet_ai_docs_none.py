while True:
    L=input()
    if int(L)<1:break
    a,t=0,0
    for i in range(12):
        k=list(map(int,input().split()))
        t+=k[0]-k[1]
        if int(L)<=t:a+=1
    print(12-a+1 if a else "NA")