a,b,x=map(int,input().split())
M=10**9+7
if b==0 or x<a:
    print(x%M)
else:
    res = x
    res += (x - a) // (a - b) * b
    res += (x - a) % (a - b)
    print(res % M)