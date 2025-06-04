from sys import exit as E
def _(_):return int(_)
n,m=map(_,input().split())
a=0
if 2*n>=m:print(m//2);E()
while n:a+=1;n-=1;m-=2
for _ in range(m//4):a+=1
print(a)