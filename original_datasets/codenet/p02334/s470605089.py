n, k = map(int, input().split( ))
mod = 10**9+7

def chs(s,t,mod):
    nume =  1
    for i in range(s-t+1,s+1):
        nume *= i
        nume %= mod
    deno = 1
    for i in range(1,t+1):
        deno *= i
        deno %= mod
    deno = pow(deno,mod-2,mod)
    
    return (nume*deno%mod)

ans = chs(n+k-1,n,mod)
print(ans)