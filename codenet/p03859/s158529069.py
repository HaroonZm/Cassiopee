"""
Writer: SPD_9X2
https://atcoder.jp/contests/arc065/tasks/arc065_d

圧倒的dp感

lは非減少なので、 l[i-1] ～l[i] の間が確定する範囲

dp[i][今の区間に残っている1の数] = 並び替えの通り数　でやると
dp推移がO(N^2)になってしまう…

1の位置さえ決まればよい。
あらかじめ、それぞれの1に関して、移動しうる最小のindexと最大のindexを前計算
→どうやって？
→heapといもす法で、最小・最大値管理しつつ

あとはdp中に一点取得、区間加算がO(N)で出来れば、O(N**2)で解ける
→dp[i個目までの1を処理][右端にある1のindex]
とし、最後に累積和で区間加算する→DP推移はO(N)なのでおｋ

→なんか違う？
→1をもってける範囲の右端が実際より短くなっているのが原因

"""
from collections import deque
import heapq
N,M = map(int,input().split())
S = input()
"""
lri = deque([])
rpick = [ [] for i in range(N+1)]
for i in range(M):
    l,r = map(int,input().split())
    lri.append([l-1,r-1,i])
    rpick[r].append(i)

lheap = []
rheap = []
state = [False] * M

LRlis = []

for i in range(N):

    while len(lri) > 0 and lri[0][0] == i: #新たに区間を入れる
        l,r,ind = lri.popleft()
        heapq.heappush(lheap,[l,ind])
        heapq.heappush(rheap,[-1*r,ind])

    for pickind in rpick[i]:

        state[pickind] = True

    while len(lheap) > 0 and state[ lheap[0][1] ]:
        heapq.heappop(lheap)
    while len(rheap) > 0 and state[ rheap[0][1] ]:
        heapq.heappop(rheap)

    if S[i] == "1":

        if len(lheap) == 0 or len(rheap) == 0:
            LRlis.append([i,i])
        else:
            LRlis.append([lheap[0][0] , -1 * rheap[0][0] ])

"""
lri = []
for i in range(M):
    l,r = map(int,input().split())
    lri.append([l-1,r-1,i])
lri.append([N,float("inf"),float("inf")])

nexvisit = 0
onenum = 0
LRlis = []
LRlisind = 0
r = 0
for loop in range(M):
    
    l,nr,tempi = lri[loop]
    r = max(nr,r)
    nexl = lri[loop+1][0]
    #print (l,r,nexl)

    for i in range( max(l,nexvisit) , r+1 ):
        if S[i] == "1":
            LRlis.append([l,None])
            onenum += 1
            nexvisit = max(nexvisit,i+1)
    if r-nexl+1 < onenum:

        for i in range(min(onenum , onenum - (r-nexl+1))):
            LRlis[LRlisind][1] = r-onenum+1
            onenum -= 1
            LRlisind += 1
            
mod = 10**9+7
dp = [0] * (N+1)
#print (LRlis)

for i in range(len(LRlis)):

    #print (dp)

    l,r = LRlis[i]

    ndp = [0] * (N+1)

    if i == 0:
        ndp[l] += 1
        ndp[r+1] -= 1
    else:

        for v in range(r):

            ndp[max(l,v+1)] += dp[v]
            ndp[r+1] -= dp[v]

    for j in range(N):
        ndp[j+1] += ndp[j]
        ndp[j] %= mod
        ndp[j+1] % mod

    dp = ndp

#print (dp)
print (sum(dp[0:N]) % mod)