import sys
import heapq

def solve():
    input = sys.stdin.readline
    while True:
        n,m = map(int,input().split())
        if n==0 and m==0:
            break

        # グラフ初期化
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        edges = [[] for _ in range(n)]

        for _ in range(m):
            a,b,c = map(int,input().split())
            a-=1
            b-=1
            dist[a][b] = c
            dist[b][a] = c
            edges[a].append((b,c))
            edges[b].append((a,c))

        # ワーシャルフロイドで最短距離
        for k in range(n):
            dk = dist[k]
            for i in range(n):
                di = dist[i]
                dik = di[k]
                for j in range(n):
                    nd = dik + dk[j]
                    if di[j]>nd:
                        di[j]=nd

        # 各局から宛先への転送先決定
        nextto = [[-1]*n for _ in range(n)]  # nextto[from][to] = 次に転送する局
        for s in range(n):
            for t in range(n):
                if s==t: 
                    continue
                candidates = []
                for (nx,cost) in edges[s]:
                    # s->nx->tの距離が最短距離に等しく，候補になる
                    if dist[s][t] == cost + dist[nx][t]:
                        candidates.append(nx)
                nextto[s][t] = min(candidates) if candidates else -1

        l = int(input())
        mails = []
        for i in range(l):
            fr, to, t, label = input().rstrip('\n').split(' ',3)
            fr = int(fr)-1
            to = int(to)-1
            t = int(t)
            mails.append({'id':i,'from':fr,'to':to,'time':t,'label':label})

        # 各郵便物は必ず配送経路が存在するので前提で処理

        # 各郵便局のキューは(郵便物到着時刻, 転送先局番号, 発送元局, 宛先局, ラベル, 物id)
        # 複数郵便物の転送先が同じならまとめて転送されたりするため、転送先毎に分けずに、
        # スケジュールで「郵便物到着時刻」「転送先局番号」の順でソート

        # 各郵便局
        pq_station = [[] for _ in range(n)]  # 配達待ちキュー： (到着時刻, 転送先局, ラベル, mailid)
        # 待機状態は転送員が局にいるかどうか
        busy = [False]*n # Falseなら転送員は局にいる
        # 次に転送員が帰ってくる時間を保持することで管理

        # mail_id -> 現在位置と到達時間管理
        # 扱いはイベント毎に郵便物を動かす

        # 配達完了時刻記録
        delivery_time = [None]*l

        # イベントキューは(時間, タイプ, 局番号, 詳細)
        # タイプは 'arrive'か'tr_return'など
        # arrive：郵便物が局に届いたイベント，（複数同時もある）

        E = []

        # 初期郵便物の出発元到着として登録
        # 郵便物が局に届くイベントを時間順にまとまって入れる
        # 到着イベントは郵便物番号でソートすることは入っていないが問題ない（同時刻は任意順）

        # まずはすべての到着イベント投入
        for mail in mails:
            heapq.heappush(E,(mail['time'],'arrive',mail['from'],mail['id']))


        # 郵便物管理（現時点でどこの局に居るかはpq_stationの中で状態管理）
        # なので、郵便物は到着時にpq_stationに格納

        # イベント処理
        while E:
            cur_t, etype, st, param = heapq.heappop(E)

            if etype=='arrive':
                # 郵便物paramが局stに到着
                mail = mails[param]
                # 宛先局であれば配達終了
                if st==mail['to']:
                    # 配達時刻記録
                    delivery_time[param]=cur_t
                    # 配達完了なので何もしない
                    continue
                # 宛先局でなければ転送局で待機
                # 転送先局は nextto[st][to]
                nxt = nextto[st][mail['to']]
                # 郵便物キューに追加
                # 優先度は(到着時刻,転送先局番号)でsort
                heapq.heappush(pq_station[st],(cur_t,nxt,mail['label'],param))

                # 転送員が局にいれば今すぐ転送開始
                if not busy[st]:
                    # 転送員が局を出る
                    busy[st] = True
                    # 転送する郵便物群を選定
                    q = pq_station[st]
                    if not q:
                        # ありえないが安全のため
                        busy[st] = False
                        continue
                    # 最優先の郵便物の転送先に合わせてまとめて転送する
                    base_arrival_time, target_nxt, _, _ = q[0]
                    # 同時刻かつ転送先が同一の郵便物をまとめて転送先に移動し、その時間に転送員は出発
                    sending = []
                    while q and q[0][0]==base_arrival_time and q[0][1]==target_nxt:
                        _,_,_,mid = heapq.heappop(q)
                        sending.append(mid)
                    # 転送時間 dist[st][target_nxt]
                    move_time = dist[st][target_nxt]
                    # 次の局に届く時刻 = cur_t + move_time
                    # 転送員は同じ時間に返ってくる → 帰還イベントを追加
                    back_time = cur_t + move_time*2
                    heapq.heappush(E,(back_time,'tr_return',st,target_nxt))
                    # 郵便物がtarget_nxt局に到着するイベントを追加 (同じ時刻に複数届く場合もある)
                    # ただし次局到着時間はcur_t + move_time
                    for mid in sending:
                        heapq.heappush(E,(cur_t+move_time,'arrive',target_nxt,mid))

            elif etype=='tr_return':
                # 転送員stが帰ってきた
                # 転送先局はparam
                # 転送員が局戻り、局内にまだ郵便物あればすぐに転送始める
                busy[st] = False
                q = pq_station[st]
                if q:
                    # 転送員が局から出発
                    busy[st] = True
                    base_arrival_time, target_nxt, _, _ = q[0]
                    sending = []
                    while q and q[0][0]==base_arrival_time and q[0][1]==target_nxt:
                        _,_,_,mid = heapq.heappop(q)
                        sending.append(mid)
                    move_time = dist[st][target_nxt]
                    back_time = cur_t + move_time*2
                    heapq.heappush(E,(back_time,'tr_return',st,target_nxt))
                    for mid in sending:
                        heapq.heappush(E,(cur_t+move_time,'arrive',target_nxt,mid))

        # delivery_timeに配達完了時刻が入った
        # 到着時刻順にソート、同時刻はラベルASCII昇順
        order = sorted([(delivery_time[i], mails[i]['label'], i) for i in range(l)], key=lambda x:(x[0],x[1]))
        for dt,label,_ in order:
            print(label,dt)
        print()

if __name__=="__main__":
    solve()