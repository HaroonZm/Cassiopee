L,N=[int(x)for x in input().split()]
s=input()
res=0
i=0
while i<L-1:
 if s[i:i+2]=='oo':
  res+=1
 i+=1
def update(l,c,n):
 for _ in range(n):
  l+=c*3
  c*=2
 return l
print(update(L,res,N))