import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa != x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False
"""
def nibu(x,n,r):
    ll = 0
    rr = r
    while True:
        mid = (ll+rr)//2

    if rr == mid:
        return ll
    if (ここに評価入れる):
        rr = mid
    else:
        ll = mid+1
"""

n = onem()
k = onem()

s = str(n)

dp0 = [[0 for j in range(4)] for i in range(len(str(n))+1)]
dp1 = [[0 for j in range(4)] for i in range(len(str(n))+1)]

po = 0

dp0[0][0] = 0
dp1[0][0] = 1

for i in range(1,len(str(n))+1):
    point = i - 1
    np = int(s[point])
    po += 1 if np == 0 else 0

    dp0[i][0] = 1
    dp1[i][0] = 0

    dp0[i][1] = dp1[i-1][0]*(max(0,np-1)) + dp0[i-1][0]*9 + dp0[i-1][1] + ( dp1[i-1][1] if np != 0 else 0 )
    dp1[i][1] = 1 if i == 1 + po else 0

    dp0[i][2] = dp1[i-1][1] * (max(0,np-1)) + dp0[i-1][1] * (9) + dp0[i-1][2] + ( dp1[i-1][2] if np != 0 else 0 )
    dp1[i][2] = 1 if i == 2 + po else 0

    dp0[i][3] = dp1[i-1][2] * (max(0,np-1)) + dp0[i-1][2] * (9) + dp0[i-1][3] + ( dp1[i-1][3] if np != 0 else 0 )
    dp1[i][3] = 1 if i == 3 + po else 0

    

print(dp0[-1][k]+dp1[-1][k])