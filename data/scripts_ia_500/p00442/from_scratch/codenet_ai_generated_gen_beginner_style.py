n=int(input())
m=int(input())
win=[[] for _ in range(n+1)]
lose=[[] for _ in range(n+1)]
degree=[0]*(n+1)
for _ in range(m):
    i,j=map(int,input().split())
    win[i].append(j)
    lose[j].append(i)

# 入力の勝敗から、「iはjに勝った」ことが分かる。
# 問題の条件より順位はトポロジカル順序で表せる。
# 1位のチームが負けなしで、n位のチームが勝ちなしであるべき。
# 条件3より「a位のチームはb位のチームに勝つ（a<b）」という方向が確定しているので、
# 入力の勝ちを参考にトポロジカルソート可能。

# 入力からは不完全な情報なのでグラフを構築し、可能な「上位→下位」の順序を推測する。

# ただし、勝敗の完全な情報は無い。なので、既知の勝敗を、
# 「勝ったチームが順位が上」にしておく。
# 他は情報なし。だから勝敗が不明なところは辺は無い扱い。
# トポロジカルソートによって一つの可能な順位が出せる。

# さらに別の順位があるかは、
# 一意性判定のため、トポロジカルソート中に複数頂点から選べるときがあるか見る。

from collections import deque

# 可能な辺の集合として入力のみを使う。
# 負の辺を入れる必要はない。全部説明されてるわけではないから。
# それで、矛盾無く、順位表が1つないし複数存在するか判定。

indeg=[0]*(n+1)
graph=[[] for _ in range(n+1)]
for i in range(1,n+1):
    for j in win[i]:
        graph[i].append(j)
        indeg[j]+=1

q=deque()
for i in range(1,n+1):
    if indeg[i]==0:
        q.append(i)

res=[]
multiple=0
while q:
    if len(q)>=2:
        multiple=1
    v=q.popleft()
    res.append(v)
    for nxt in graph[v]:
        indeg[nxt]-=1
        if indeg[nxt]==0:
            q.append(nxt)

# resがnなら解がある。そうでなければ矛盾。
# 問題文では「伝えられた情報に適合する順位表」があるという仮定。

for x in res:
    print(x)
print(multiple)