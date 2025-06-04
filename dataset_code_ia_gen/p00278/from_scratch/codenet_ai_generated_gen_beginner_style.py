import sys
import bisect

input=sys.stdin.readline

N,Q=map(int,input().split())
scores=[int(input()) for _ in range(N)]

leaders=set()
leader_scores=[]

def count_unable_to_join(r):
    # グループに入れない生徒の数を数える（リーダーがいる状態で）
    if not leaders:
        # リーダーがいなければ全員参加不可
        return N
    groups=sorted(leader_scores)
    unable=0
    for i in range(N):
        s=scores[i]
        # sより小さいリーダースコアに参加不可
        # 参加できるリーダーは s >= leader_score and s < leader_score + r + 1
        # 条件より s >= leader_score と s <= leader_score + r
        # リーダースコア s_leader <= s <= s_leader + r
        # s_leader <= s なので s_leader <= s
        # s <= s_leader + r
        # つまり s - r <= s_leader <= s とリーダースコアがこの範囲にある必要がある
        # s - r <= leader_score <= s
        left=s - r
        # left以上でleader_scoresのindexを取得
        idx=bisect.bisect_left(groups, max(left,0))
        found=False
        # idxからs以下のleader_scoresを探す
        while idx < len(groups) and groups[idx] <= s:
            found=True
            break
        if not found:
            unable+=1
    return unable


for _ in range(Q):
    query=input().split()
    if query[0]=="ADD":
        a=int(query[1])-1
        if a not in leaders:
            leaders.add(a)
            bisect.insort(leader_scores, scores[a])
    elif query[0]=="REMOVE":
        a=int(query[1])-1
        if a in leaders:
            leaders.remove(a)
            idx=bisect.bisect_left(leader_scores,scores[a])
            # リストは複数同じ値があるかもしれないけどaはuniqueなので最初にあったら消す
            del leader_scores[idx]
    else: # CHECK x
        x=int(query[1])
        if not leaders:
            # リーダーいなければ全員参加不可
            if x>=N:
                print(0)
            else:
                print("NA")
            continue
        # 二分探索でrを探す
        left=0
        right=10**10
        answer=-1
        while left<=right:
            mid=(left+right)//2
            unable=count_unable_to_join(mid)
            if unable <= x:
                answer=mid
                right=mid-1
            else:
                left=mid+1
        if answer==-1 or answer>10**9:
            print("NA")
        else:
            print(answer)