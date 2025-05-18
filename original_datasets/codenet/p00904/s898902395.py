for _ in range(int(input())):
    p,q=map(int,input().split())
    c=0
    for i in range(142):
        for j in range(142):
            if (i>0 or j>0)and(j*p+i*q)%(j*j+i*i)==0 and (j*q-i*p)%(j*j+i*i)==0:c+=1
    print('P' if c<5 else 'C')