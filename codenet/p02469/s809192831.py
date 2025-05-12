import fractions
n=int(input())
l=list(map(int,input().split()))

m=l[0]
for i in range(n):
    m=m*l[i]//fractions.gcd(m,l[i])
print(m)