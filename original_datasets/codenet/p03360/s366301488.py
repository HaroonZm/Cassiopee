A,B,C = map(int,input().split())
K = int(input())

def dfs(i,a,b,c):
    if i == K:
        return A*(2**a)+B*(2**b)+C*(2**c)
    res1 = dfs(i+1,a+1,b,c)
    res2 = dfs(i+1,a,b+1,c)
    res3 = dfs(i+1,a,b,c+1)
    return max(res1,res2,res3)

print(dfs(0,0,0,0))