x,y=map(int,input().split())
def gcd(a,b):
    while b:b,a=b,a%b
    return a
print(x+y-gcd(x,y))