import sys
import heapq

# 東西方向の道路名 (a,b,c,...) と南北方向の道路番号 (1,2,3,...) を交差点として扱うための関数群

def parse_cross_point(s):
    # 交差点の文字列 "a-1" から (x, y) 座標 (0-indexed) に変換
    # x: 東西方向の道路 index (a->0,b->1,...)
    # y: 南北方向の道路 index (1->0,2->1,...)
    h,v = s.split('-')
    x = ord(h) - ord('a')
    y = int(v) -1
    return (x,y)

def cross_point_str(x,y):
    # (x, y) 座標から "a-1" の文字列に戻す関数（今回は不要だが解析用に用意）
    return chr(ord('a')+x) + '-' + str(y+1)

def get_direction(u,v):
    # u,v は (x,y)
    # uからvへの直進方向を示す文字: 'N','S','E','W'
    ux, uy = u
    vx, vy = v
    if ux == vx:
        if vy == uy+1:
            return 'S'  # 南へ
        elif vy == uy-1:
            return 'N'  # 北へ
    elif uy == vy:
        if vx == ux+1:
            return 'E'  # 東へ
        elif vx == ux-1:
            return 'W'  # 西へ
    return None

def opposite_dir(d):
    return {'N':'S','S':'N','E':'W','W':'E'}[d]

# 信号の判定用関数 (時間 t 分時点で信号が東西方向に青か南北方向に青か判定)
def is_signal_green_NS(t, k):
    # 問題文: 信号の周期は k 分，現在は t 分時点で
    # 一旦初期条件としてt=0で南北方向が青 -> (t//k)が偶数なら南北青(東西赤)
    # (t//k)が奇数なら東西が青(南北赤)
    return (t // k) % 2 == 0

# 入力を読み込んでデータセットごとに処理する関数
def solve():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        M, N = map(int,line.split())
        if M==0 and N==0:
            break
        D = int(input())
        ns = int(input())

        # 信号機情報: 各交差点ごとに周期を登録。信号が無い交差点は無し
        signals = dict()
        for _ in range(ns):
            s,k = input().split()
            k = int(k)
            pos = parse_cross_point(s)
            signals[pos] = k

        # 工事中の道路
        nc = int(input())
        closed_roads = set()
        for _ in range(nc):
            s1,s2 = input().split()
            p1 = parse_cross_point(s1)
            p2 = parse_cross_point(s2)
            # 通行できない道路は両方向扱う
            closed_roads.add((p1,p2))
            closed_roads.add((p2,p1))


        # 渋滞道路と渋滞度
        nj = int(input())
        congest_roads = dict()
        for _ in range(nj):
            s1,s2,d = input().split()
            d = int(d)
            p1 = parse_cross_point(s1)
            p2 = parse_cross_point(s2)
            # こちらも両方向に同じ渋滞度
            congest_roads[(p1,p2)] = d
            congest_roads[(p2,p1)] = d

        # 始点と終点
        s,dst = input().split()
        start = parse_cross_point(s)
        goal = parse_cross_point(dst)

        # 市内の交差点はグリッドの交差点数 (M* N)
        # 頂点は (x,y), 0 <= x < M, 0 <= y < N

        # 移動方向：東西方向の道路でxが変わる、南北方向でyが変わる
        # サンプルより、東西がM本で x=[0..M-1]
        # 南北がN本で y=[0..N-1]

        # 移動可能か確認と辺の設定
        # 2方向通行なので上下左右4方向チェック、ただしUターン禁止：
        # 「トラックは交差点で方向変換可能だが、来た方向には戻れない」

        # 最短時間は状態を(位置(x,y), 向き) で管理してDijkstraで探索する
        # 向きは 'N','S','E','W' の4通り

        # 初期条件: トラックは東向きで出発
        start_dir = 'E'

        # 状態数は M*N*4で最大 20*20*4=1600なのでDijkstra可能

        # 探索
        # 到着時刻 t で次の道路に進むためには、
        # 1. 現在の交差点到着時間 t を知る
        # 2. 次の交差点へ向かう方向を決める（Uターン禁止なので逆方向は不可）
        # 3. 次の移動時間は D + 渋滞時間 d_i
        # 4. 次の交差点到着時刻 t_next = t + 移動時間
        # 5. 次の交差点に信号がある場合、t_next の信号の状態によっては進入不可
        #   - 赤なら進入できず、到着まで待った時間も含めて計算し、
        #     待った後の信号が青になる瞬間まで待つ必要がある。
        # 6. 次の移動開始時刻は交差点で速度低下無し（信号開通待ちは移動時刻ではなく待ち時間）
        # 7. 整数時間を分単位とし、信号の切り替わり時間も整数分なので、初めから整数時間で扱える。

        # 信号の進入判定は「交差点に到着した時刻に信号が赤なら入れない」なので
        # 待ち時間も含めてt_nextを調整する必要がある。
        # ただしトラックが交差点に着くまで信号判定し、赤なら待つ処理を行い、
        # これは道路の出発前に待つことになるので、
        # 移動前に信号の赤待ち判定は「次の交差点で待つ」ではなく、「次の交差点に入るための待ち」とみなす。

        # → 信号待ちの実装としては、交差点に入る時刻t_nextが赤なら、
        # 到達時刻をt_nextから次の青時間まで増やす

        # 初期状態で10^9ぐらいで距離を初期化し、優先度付きキューで解く

        INF = 10**9
        dist = dict() # key=(x,y,dir), value=最短時間
        # 初期状態
        hq = []
        # (cost, x,y, direction)
        heapq.heappush(hq, (0, start[0], start[1], start_dir))
        dist[(start[0],start[1],start_dir)] = 0

        # 方向ベクトル
        directions = {
            'N': (0,-1),
            'S': (0,1),
            'E': (1,0),
            'W': (-1,0)
        }
        # 方向の選択肢（Uターン禁止で4方向中3方向選択可能）
        all_dirs = ['N','S','E','W']

        # 交差点が存在する範囲確認関数
        def in_grid(x,y):
            return 0 <= x < M and 0 <= y < N

        # 信号判定(次の交差点に進入時刻t_nextが赤なら待ち時間を追加してt_nextを青まで待つ時間を増やす)
        def adjust_arrival_for_signal(pos, t_next):
            # pos は次の交差点 (x,y)
            if pos in signals:
                k = signals[pos]
                # 現時刻t_nextで南北方向が青か東西方向が青か判定
                # 青の方向がどちらかによって許可される方向が違う
                # 信号は交差点の信号で交差点通過の際、進入できるか判定

                # まずこの交差点の信号周期kを取得しt_nextを使って現在の色を判定

                # 移動方向 (u->pos) の方向を判定
                # この関数では移動方向情報はないので下流で事前に調べて渡す必要あり
                # しかし今は渡せないので、調整は移動先で行うため、
                # 方向は別に判定する必要があるため adjust_arrival_for_signal 呼び出し前に
                # 移動方向を計算し呼び出す形に修正する。
                # → 呼び出し箇所で方向も渡す形に変更する。

                return t_next
            else:
                return t_next

        # 信号判定改良：入る向きでも判定。東西方向か南北方向か判定
        # 入る方向 d -> 移動方向
        # 信号の青は南北か東西か
        # 東西が青なら東か西の進入はOK、それ以外(南か北)は赤待ちする必要あり

        def adjust_arrival_for_signal_with_direction(pos, t_next,d):
            if pos in signals:
                k = signals[pos]
                ns_green = is_signal_green_NS(t_next, k)
                # ns_green==True => 南北が青、東西が赤
                if d in ['N','S']:
                    # 進入方向が南北方向
                    if ns_green:
                        # 青なので入れる
                        return t_next
                    else:
                        # 赤なので次の青まで待つ
                        # k分周期でt_nextの次の周期開始まで待つ
                        wait = (k - (t_next % k)) if (t_next % k) != 0 else 0
                        return t_next + wait
                else:
                    # 進入方向が東西方向
                    if ns_green:
                        # 赤なので待つ
                        wait = (k - (t_next % k)) if (t_next % k) != 0 else 0
                        return t_next + wait
                    else:
                        # 青なのでOK
                        return t_next
            else:
                return t_next

        while hq:
            cost,x,y,d = heapq.heappop(hq)
            state = (x,y,d)
            if dist.get(state, INF) < cost:
                continue
            if (x,y) == goal:
                print(cost)
                break
            # 現状態で(x,y,d)で次の移動可能方向を選ぶ。ただしUターンは禁止
            for nd in all_dirs:
                if nd == opposite_dir(d):
                    continue
                dx,dy = directions[nd]
                nx, ny = x+dx, y+dy
                if not in_grid(nx,ny):
                    continue
                # 道路の状態を調べる
                u = (x,y)
                v = (nx,ny)
                if (u,v) in closed_roads:
                    continue

                # 移動時間 = D + 渋滞なら d_i
                time = D
                if (u,v) in congest_roads:
                    time += congest_roads[(u,v)]

                arrival = cost + time

                # 交差点に到着する時間 arrival で信号判定
                # 移動方向がndなのでこれを渡す
                arrival_adj = adjust_arrival_for_signal_with_direction(v, arrival, nd)

                # arrival_adj >= arrival なので信号待ちしている間はここに余分な待時間が入る

                next_state = (nx, ny, nd)
                if dist.get(next_state, INF) > arrival_adj:
                    dist[next_state] = arrival_adj
                    heapq.heappush(hq, (arrival_adj, nx, ny, nd))

if __name__=="__main__":
    solve()