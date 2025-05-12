import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**7) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

s = ns()
t = ns()

lens = len(s)
lent = len(t)

dp = [[0]*(lent+1) for _ in range(lens+1)]

for idx in range(lens):
    for jdx in range(lent):
        dp[idx+1][jdx+1] = max(dp[idx][jdx] + bool(s[idx] == t[jdx]),
                               dp[idx+1][jdx],
                               dp[idx][jdx+1])
    
def lcs(spos: int, tpos: int, cur: str, s:str, t:str, dp: list) -> str:

    if spos == 0 or tpos == 0:
        return cur
    
    else:
        nrth = dp[spos-1][tpos]
        west = dp[spos][tpos-1]
        ntws = dp[spos-1][tpos-1]

        mx = max(nrth, west, ntws)
        
        if mx == ntws and ntws+1 == dp[spos][tpos]:
            return lcs(spos-1, tpos-1, cur+s[spos-1], s,t,dp)
 
        
        elif mx == nrth:
            return lcs(spos-1, tpos, cur, s, t, dp)
        
        else:
            return lcs(spos, tpos-1, cur, s, t, dp)
            
           

            
            
print(lcs(lens, lent, "", s, t, dp)[::-1])