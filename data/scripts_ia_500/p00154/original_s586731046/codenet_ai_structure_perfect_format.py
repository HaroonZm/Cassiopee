import sys
readline=sys.stdin.readline
write=sys.stdout.write
ans=[]
while 1:
    M=int(readline())
    if M==0:
        break
    P=[list(map(int,input().split())) for i in range(M)]
    memo={}
    def dfs(i,rest):
        if i==M:
            return rest==0
        key=(i,rest)
        if key in memo:
            return memo[key]
        res=0
        a,b=P[i]
        for j in range(0,b+1):
            if rest-j*a<0:
                break
            res+=dfs(i+1,rest-j*a)
        memo[key]=res
        return res
    G=int(input())
    for i in range(G):
        ans.append(str(dfs(0,int(input()))))
write("\n".join(ans))
write("\n")