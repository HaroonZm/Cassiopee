import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

while True:
    n=int(input())
    if n==0:
        break
    p=[0]*(n+1)
    q=[0]*(n+1)
    r=[0]*(n+1)
    b=[0]*(n+1)
    for i in range(1,n+1):
        pp,qq,rr,bb=map(int,input().split())
        p[i]=pp
        q[i]=qq
        r[i]=rr
        b[i]=bb

    # dp[i]: (weight of balanced subtree rooted at i with the minimal weights assignment)
    # weight[i]: integer weight assigned to the node
    # We'll do post-order dfs to compute minimal weights

    weight = [0]*(n+1)
    memo = {}

    def dfs(x):
        if x==0:
            return 1  # weight of a single weight is 1

        if x in memo:
            return memo[x]

        lw = dfs(r[x])  # left weight (red side)
        rw = dfs(b[x])  # right weight (blue side)

        # We want integer weights a,b such that:
        # a*p[x] = b*q[x], a >= lw, b >= rw
        # minimal total weight a + b

        # start from lw and rw, scale to match ratio:
        # Find minimal k so that:
        # a = p[x]*k >= lw
        # b = q[x]*k >= rw
        # so k >= ceil(lw / p[x]) and k >= ceil(rw / q[x])

        # but since lw,rw and p[x],q[x] are integers, we can do:
        # find k such that max((lw + p[x]-1)//p[x], (rw + q[x]-1)//q[x]) <= k
        # then a = p[x]*k, b = q[x]*k

        a_min = (lw + p[x]-1)//p[x]
        b_min = (rw + q[x]-1)//q[x]
        k = max(a_min,b_min)
        a = p[x]*k
        b = q[x]*k
        memo[x] = a + b
        return memo[x]

    print(dfs(1))