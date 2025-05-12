import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
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

n,k = m()

a = l()

aaa = [0 for i in range(n)]
co = [0 for i in range(2002)]

for i in range(n-1,-1,-1):
    aaa[i] = co[a[i]]
    for j in range(a[i]+1,2000+2):
        co[j] += 1

su = 0

for i in range(n-1,-1,-1):
    su += k * aaa[i]
    su %= mod
    su += (((k)*(k-1))//2)*co[a[i]]
    su %= mod

print(su)