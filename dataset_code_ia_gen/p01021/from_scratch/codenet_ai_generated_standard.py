import math
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)
N,M=map(int,input().split())
A=[int(input()) for _ in range(N)]
B=list(map(int,input().split()))
L=1
for a in A:
    L=lcm(L,a)
G=0
for b in B:
    G=gcd(G,b)
count=0
if L%G==0:
    max_k=G//L
    for k in range(1,max_k+1):
        if G%(L*k)==0:
            count+=1
print(count)