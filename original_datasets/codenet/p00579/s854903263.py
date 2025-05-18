# siawaseegoisuto273さんのものを参考にした。(pythonで書いた)
#

# N, Mの数
N, M = map(int, input().split())
L = [0] * M
R = [0] * M

# 明るさ
A = list(map(int, input().split()))

# 制約条件
for i in range(M):
    L[i], R[i] = map(int, input().split())
    
pre = [0] * (N+1)
dp = [0] * (N+1)

# 制約条件の書き換え
# pre[i]は、位置iが含まない制約の番号の最大を表す(ただしiより小さい)
# pre[i]が0は、同一の制約の中にi=1が含まれることを表す。
# preの作成のアルゴリズムが一番むずかしい
#
# 1. 
# R[i]の値を配列の位置情報(何番目)で表現する。
# pre[R[i]]は、L[i]の情報を表す(正確にはL[i]-1)
# ※制約条件は広い方に吸収される
# (R[i], L[i]) = {(4, 5), (3, 5), (6, 9), (7, 8), (10, 11), (10, 13)}
#              ->{(3, 5), (6, 9), 10, 13} となる。
#
# 2. 条件の隅の情報しか更新していないため、最後に後ろから値を詰めていって、完成する。
# 

# 制約の初期化
for i in range(1, N+1):
    pre[i] = i - 1

# 制約条件に含まれない左側
for i in range(M):
    pre[R[i]] = min(pre[R[i]], L[i]-1)
    # print("print pre")
    # print(pre)
    # print("")
    
for i in range(N-1, 0, -1):
    pre[i] = min(pre[i], pre[i+1])
    # print("print pre2")
    # print(pre)
    # print("")

# 動的計画法を解いていく
# 小さい方から値を詰めていく
for i in range(1, N+1):
    dp[i]=max(dp[i-1], dp[pre[i]] + A[i-1])
    # print(dp)

print(dp[N])