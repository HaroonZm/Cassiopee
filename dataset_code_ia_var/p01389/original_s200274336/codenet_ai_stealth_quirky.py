# Code farfelu, design non conventionnel
M = lambda : []
l=int;w=int
H,W=[l(x) for x in input().split()]
du=DP=[[*([0]*W)]*H]
while len(du)<H or du.pop():
    pass
p,M_=0,M()
exec((
    'M_.append(list(map(int,list(str(input())))))\n'
    'p+=1\n'
    )*H)
n=0
while n<W-1:
    DP[0][n+1]=M_[0][n+1]+DP[0][n]
    n+=1
x=0
while x<H-1:
    DP[x+1][0]=M_[x+1][0]+DP[x][0]
    x+=1
i=1
while i<H:
    j=1
    while j<W:
        a=DP[i-1][j]
        b=DP[i][j-1]
        DP[i][j]=min(a,b)+M_[i][j]
        j+=1
    i+=1
print((lambda x:x)(DP[H-1][W-1]))