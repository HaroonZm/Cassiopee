import sys
input=sys.stdin.readline

notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
note_idx = {n:i for i,n in enumerate(notes)}
def up(n): return notes[(note_idx[n]+1)%12]
def down(n): return notes[(note_idx[n]-1)%12]

ds = int(input())
for _ in range(ds):
    n,m = map(int,input().split())
    T = input().split()
    S = input().split()
    # 状態は(段,k) k=0..m演奏済みかどうか
    # k=曲のどの位置まで演奏したか
    # 0段目は雲、n+1段目は地上（存在）
    from collections import deque
    visited = [False]*(n+2)
    # 初期は雲0段目で曲0演奏済み
    # キューに(段,k)
    que=deque()
    que.append((0,0))
    vis = [set() for _ in range(n+2)]
    vis[0].add(0)
    ans="No"
    while que:
        pos,k = que.popleft()
        if pos==n+1 and k==m:
            ans="Yes"
            break
        # 次の移動可能段を列挙
        # 次に踏む段とそこからの音のパターンを判定
        candidates=[]
        # 0段目は離れたら戻れず-1いけない
        # 0->-1 無意味
        if pos>0:
            candidates.append(pos-1)
        if pos+1<=n+1:
            candidates.append(pos+1)
        if pos+2<=n+1:
            candidates.append(pos+2)
        for nxt in candidates:
            # 鳴る音判定
            if pos==0:
                # 0段目から出て戻れないから-1なし
                # 動けるのは1 or 2段目のみだが2段目は存在しないかもしれないので条件は上で
                if nxt==pos+1:
                    this_sound = T[nxt-1]
                elif nxt==pos+2:
                    this_sound = up(T[nxt-1])
                else:
                    continue
            else:
                if nxt==pos-1:
                    this_sound=down(T[nxt-1])
                elif nxt==pos+1:
                    this_sound=T[nxt-1]
                elif nxt==pos+2:
                    this_sound=up(T[nxt-1])
                else:
                    continue
            # 地上(n+1段目)は音階無し、n+1段目から動けないのでここでの判定
            if nxt==n+1:
                # 曲はこれでk==mでないとダメ
                if k==m and pos!=0:
                    if k not in vis[nxt]:
                        vis[nxt].add(k)
                        que.append((nxt,k))
                continue
            # 曲の次に期待する音はS[k] (演奏済みk番目)
            if k<m and this_sound==S[k]:
                nk = k+1
            else:
                nk = k
            # 0段目には戻れない(0=>0は無いし0=>0は動けない)
            if nxt==0 and pos!=0:
                continue
            if nk not in vis[nxt]:
                vis[nxt].add(nk)
                que.append((nxt,nk))
    print(ans)