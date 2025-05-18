def f(n):
    a=[]
    while n%2==0:
        a.append(2)
        n=n//2
    f=3
    while f*f<=n:
        if n%f==0:
            a.append(f)
            n=n//f
        else:
            f+=2
    if n!=1:
        a.append(n)
    return(a)
    
n=int(input())
a=f(n)
b=[str(i) for i in a]
A=" ".join(b)
print(f"{n}: {A}")