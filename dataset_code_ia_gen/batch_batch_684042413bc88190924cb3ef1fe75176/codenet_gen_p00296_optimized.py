import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

class Node:
    __slots__ = ('val','prev','next')
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

N,M,Q=map(int,input().split())
a=list(map(int,input().split()))
q=list(map(int,input().split()))

# 初期円環作成
nodes=[Node(i) for i in range(N)]
for i in range(N):
    nodes[i].next=nodes[(i+1)%N]
    nodes[i].prev=nodes[(i-1)%N]

present=set(range(N))
cur=nodes[0]  # 最初にバトンを持つ生徒

for x in a:
    # 移動方向決定
    if x%2==0:
        # 時計回り
        for _ in range(x):
            cur=cur.next
    else:
        # 反時計回り
        for _ in range(x):
            cur=cur.prev
    # curは脱落生徒
    present.discard(cur.val)
    # バトンは脱落生徒の時計回り隣に移る
    nxt=cur.next
    # 脱落生徒を円環から除去
    cur.prev.next=cur.next
    cur.next.prev=cur.prev
    cur=nxt

res=[1 if x in present else 0 for x in q]
print('\n'.join(map(str,res)))