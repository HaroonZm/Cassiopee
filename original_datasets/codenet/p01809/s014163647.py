def gcd(a, b):
    while b: a, b = b, a % b
    return a

a,b=map(int,input().split())
b//=gcd(a,b)
a,c=2,1
while a*a<=b:
    if b%a==0:
        c*=a
        while b%a==0:b//=a
    a+=1
print([c*b,c][b==1])