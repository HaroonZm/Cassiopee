while 1:
    n=int(input())
    if n==0:break
    s=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            s.append(i)
            s.append(n//i)
    s=list(set(s))
    s.remove(n)
    if sum(s)==n:
        print("perfect number")
    elif sum(s)<n:
        print("deficient number")
    elif sum(s)>n:
        print("abundant number")