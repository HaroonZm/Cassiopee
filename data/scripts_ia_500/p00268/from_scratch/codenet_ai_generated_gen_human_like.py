import sys
sys.setrecursionlimit(10**7)

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

def intersect(p1, p2, p3, p4):
    # 線分(p1,p2)と(p3,p4)の交差判定
    c1 = ccw(p1, p2, p3)
    c2 = ccw(p1, p2, p4)
    c3 = ccw(p3, p4, p1)
    c4 = ccw(p3, p4, p2)
    if c1 * c2 == 0 and c3 * c4 == 0:  # 線分が重なっている場合
        return False
    return (c1 * c2 < 0) and (c3 * c4 < 0)

def point_in_polygon(point, polygon):
    # ray casting法で多角形内判定（点が多角形の内部or境界上にあるか）
    x,y = point
    cnt = 0
    for i in range(len(polygon)):
        x1,y1 = polygon[i]
        x2,y2 = polygon[(i+1)%len(polygon)]
        if y1>y2:
            x1,y1,x2,y2 = x2,y2,x1,y1
        if y == y1 or y==y2:
            y += 1e-10  # 境界線上のケース回避
        if y > y1 and y<y2:
            crossx = (y - y1)*(x2 - x1)/(y2 - y1) + x1
            if crossx > x:
                cnt +=1
    return cnt %2 ==1

def solve():
    input=sys.stdin.readline
    while True:
        C,W= map(int,input().split())
        if C==0 and W==0:
            break
        pillars=[]
        for _ in range(C):
            x,y = map(int,input().split())
            pillars.append((x,y))
        walls=[]
        for _ in range(W):
            s,t= map(int,input().split())
            walls.append((s-1,t-1))

        # お屋敷は凸多角形（柱をつなげた多角形）
        polygon = pillars[:]

        # 部屋の判別：壁で区切られた部屋と外で構成される。ここで考慮するのは、
        # 各壁の穴は、その部屋間の移動に利用される。
        # まず壁がどの部屋を仕切っているかを調べる。
        # 部屋を番号付けするための準備
        # 壁上に壁方向に少しずらした点を2点生成し、その点が多角形内部か外部かで部屋を区別

        # 部屋番号は、壁の両側の空間を部屋番号で示すため、壁ごとに左側、右側の空間を検査
        # 部屋IDは連番で管理。外は0にする。

        room_id_map = {} # (壁番号, 0 or 1) => 部屋番号
        room_positions = [] # 部屋番号ごとの代表点（内側のどこかの座標）

        # 外=部屋番号0
        room_count = 1

        def midpoint(a,b):
            return ((a[0]+b[0])/2, (a[1]+b[1])/2)

        # ポリゴンの辺は柱番号で連続しているとは限らないが、問題の制約により柱をつなげた凸多角形が建物外周。
        # 多角形の辺は柱番号の順番に対応すると考えて良い。

        # 建物外周の辺の集合
        poly_edges=set()
        for i in range(C):
            poly_edges.add((i,(i+1)%C))
            poly_edges.add(((i+1)%C,i))

        # 点を壁から少しずらして部屋外部か部屋内部判定
        def get_side_point(p1,p2,distance=1e-5):
            # p1->p2 ベクトルに垂直な方向にdistanceだけずらした点を2つ返す
            dx = p2[0]-p1[0]
            dy = p2[1]-p1[1]
            length = (dx*dx+dy*dy)**0.5
            ux = dx/length
            uy = dy/length
            # 左側方向ベクトル (-uy, ux)
            leftx = (p1[0]+p2[0])/2 - uy*distance
            lefty = (p1[1]+p2[1])/2 + ux*distance
            # 右側方向ベクトル (uy, -ux)
            rightx = (p1[0]+p2[0])/2 + uy*distance
            righty = (p1[1]+p2[1])/2 - ux*distance
            return (leftx,lefty),(rightx,righty)

        # 部屋番号割り当て用辞書に外=0を設定
        room_id_map = {}
        room_points = []

        def room_find(pt):
            # 新しい部屋候補か調べ、あれば番号を返す、なければ新規追加
            for i,p in enumerate(room_points):
                # 同じ部屋なら距離が近いはずなので小さな閾値で判定
                d = (p[0]-pt[0])**2+(p[1]-pt[1])**2
                if d < 1e-6:
                    return i
            # 新規追加
            room_points.append(pt)
            return len(room_points)-1

        # 外部か内部か判定
        def inside_polygon(pt):
            return point_in_polygon(pt, polygon)

        # 各壁の両側の部屋IDを求める
        wall_rooms = []
        for i,(s,t) in enumerate(walls):
            p1 = pillars[s]
            p2 = pillars[t]
            left_pt,right_pt = get_side_point(p1,p2)
            left_in = inside_polygon(left_pt)
            right_in = inside_polygon(right_pt)
            if left_in and right_in:
                # 壁両側は部屋内？普通は無いはず
                # 部屋分割している壁なら問題発生だが、問題条件から「壁は部屋同士か部屋と外を仕切る」
                # 同時に凸多角形の中なので、ありえない。とりあえず左を部屋、右を別部屋扱い
                left_id = room_find(left_pt)
                right_id = room_find(right_pt)
            elif left_in:
                left_id = room_find(left_pt)
                right_id =0
            elif right_in:
                right_id = room_find(right_pt)
                left_id = 0
            else:
                # 両方外？建物外にある壁は無いはずなので左を外で右を外にしておく（理論上ありえない）
                left_id=0
                right_id=0
            wall_rooms.append((left_id,right_id))

        # 部屋数
        room_num = len(room_points)
        # 部屋graph構築（穴がある壁に対応）
        graph = [[] for _ in range(room_num+1)]  # 0は外

        for i,(r1,r2) in enumerate(wall_rooms):
            if r1 != r2:
                graph[r1].append(r2)
                graph[r2].append(r1)

        # 部屋ごとから外(=0)への最短距離(穴通過数)を計算
        from collections import deque
        dist = [-1]*(room_num+1)
        dist[0]=0
        queue=deque([0])
        while queue:
            cur = queue.popleft()
            for nxt in graph[cur]:
                if dist[nxt]==-1:
                    dist[nxt]= dist[cur]+1
                    queue.append(nxt)

        # 部屋0は外なので除外して最大値を求める
        max_dist = 0
        for i in range(1, room_num+1):
            if dist[i] > max_dist:
                max_dist = dist[i]

        print(max_dist)

if __name__=="__main__":
    solve()