a,b,n=list(map(int,input().split()))
if n%500!=0:n=n+500-n%500
if a>=b*2:
    print((n//500)*b)
elif a<b:
    if n%1000!=0:n=n+1000-n%1000
    print((n//1000)*a)
else:
    print(((n//1000)*a)+((n%1000)//500)*b)