import sys
import heapq
input=sys.stdin.readline

N,M,X=map(int,input().split())
T=[int(input()) for _ in range(N)]

adj=[[] for _ in range(N)]
for _ in range(M):
    a,b,d=map(int,input().split())
    a-=1
    b-=1
    adj[a].append((b,d))
    adj[b].append((a,d))

INF=10**15
# 状態: (時間, 部屋, 最後に寒いか暑い部屋出てからの経過時間, 最後の温度カテゴリ)
# 最後の温度カテゴリ: 0=寒い部屋、1=快適、2=暑い部屋、3=初期状態(部屋1が寒いので0で開始)
# 快適な部屋は制約なし，寒/暑はX分ルールがある
dist=[[[INF]*(X+1) for _ in range(3)] for _ in range(N)]
# 初期状態は部屋1(0), 最後に寒い部屋にいたのでlast=0, elapsed=0
dist[0][0][0]=0
hq=[(0,0,0,0)] # (時間, 部屋, last温度, elapsed)

while hq:
    time,v,last,elapsed=heapq.heappop(hq)
    if dist[v][last][elapsed]<time:
        continue
    if v==N-1:
        print(time)
        break
    for nv,d in adj[v]:
        tn=T[nv]
        # 移動後のlast,elapsedを計算
        if tn==1:
            # 快適: elapsed=0, last同じまま
            nlast=last
            nelapsed=0
        else:
            if tn==0:
                cur=0
            else:
                cur=2
            if last==1: # 今まで快適ならlast=cur, elapsed=0
                nlast=cur
                nelapsed=0
            else:
                # last=0 or 2でcur=0 or 2の時禁止ならスキップ
                if last!=cur and elapsed+ d<X:
                    continue
                # else elapsedは0に戻る
                nlast=cur
                nelapsed=0
        # 更新(elapsed+ d capped by X)
        # 快適は0に戻ってるのでelse部分のみで時間加算は反映済み
        nt=time+d
        if dist[nv][nlast][nelapsed]>nt:
            dist[nv][nlast][nelapsed]=nt
            heapq.heappush(hq,(nt,nv,nlast,nelapsed))