n,k=map(int,input().split())
o=n//k
p=0
if (k%2==0): p=(n+(k//2))//k
print(o**3+p**3)