def getN():return int(input())
def getlist():return list(map(int,input().split()))

def solve(n,pos):
 xy=pos
 x,y=xy
 x=n-x+1 if x>n//2 else x
 y=n-y+1 if y>n//2 else y
 color= ((min(x,y)-1)%3)+1 if x!=y else (((x-1)%3)+1)
 return color

n=getN()
k=getN()
[print(solve(n,getlist())) for _ in range(k)]