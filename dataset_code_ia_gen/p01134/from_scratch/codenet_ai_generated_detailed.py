import sys
import math

# 定数設定
EPS = 1e-10

# 点の表現用（x, y）
def dist(p1, p2):
    """2点間の距離を計算"""
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def is_close(p1, p2):
    """2点が近接しているか判定"""
    return dist(p1, p2) < EPS

def line_intersection(A1, A2, B1, B2):
    """
    2つの線分A1A2とB1B2の交点を求める。
    入力は端点座標。交点が存在しない場合はNoneを返す。
    """
    # 線分のベクトル
    dxA = A2[0] - A1[0]
    dyA = A2[1] - A1[1]
    dxB = B2[0] - B1[0]
    dyB = B2[1] - B1[1]

    # 連立方程式の計算： A1 + tA*(A2 - A1) = B1 + tB*(B2 - B1) を解く
    denom = dxA * dyB - dyA * dxB
    if abs(denom) < EPS:
        # 平行または一致（問題文で重なることはないとしている）
        return None

    tA = ((B1[0] - A1[0]) * dyB - (B1[1] - A1[1]) * dxB) / denom
    tB = ((B1[0] - A1[0]) * dyA - (B1[1] - A1[1]) * dxA) / denom

    # tA, tBが0-1の範囲であれば線分上の交点
    # ただし直線同士の交点を求めたいので線分判定しないでよい
    # ここは直線同士の交点なので判定なし
    intersect_x = A1[0] + tA * dxA
    intersect_y = A1[1] + tA * dyA
    return (intersect_x, intersect_y)

def is_point_on_segment(P, A, B):
    """
    点Pが線分AB上にあるか判定
    """
    dAB = dist(A, B)
    dAP = dist(A, P)
    dPB = dist(P, B)
    # 三角不等式の緩いイコール（誤差考慮）
    return abs(dAP + dPB - dAB) < EPS

def clip_line_to_square(p1, p2, square_border):
    """
    線分p1-p2を正方形の中に切り取る。
    入力点は正方形辺上の点なので、線は必ず正方形内を通る。
    ただし線は無限延長線として考えるべきなので、
    この関数は正方形との交点２点を返す。
    """
    # 正方形の4辺をそれぞれ線と交差判定
    # 4辺は[(start, end), ...]
    edges = [
        ((-100, -100), (100, -100)),
        ((100, -100), (100, 100)),
        ((100, 100), (-100, 100)),
        ((-100, 100), (-100, -100))
    ]
    intersections = []
    for edge_start, edge_end in edges:
        inter = line_intersection(p1, p2, edge_start, edge_end)
        if inter is not None:
            if is_point_on_segment(inter, edge_start, edge_end):
                if is_point_on_segment(inter, p1, p2) or True:
                    # 交点が正方形の辺上にあるなら記録
                    # p1-p2は辺上の2点なので直線が必ず正方形通過
                    # ここは直線としての交点は有効
                    # ただし線分判定でなく正方形範囲確認に利用
                    if not any(is_close(inter, ex) for ex in intersections):
                        intersections.append(inter)
    # intersectionsは2点あるはずなのでソートして返す
    # もし入力点2点が違う辺上にあり問題文条件でそうなる
    if len(intersections) != 2:
        # 問題文の条件で必ず２点
        # ただ念のためp1,p2で代用
        intersections = [p1, p2]
    # ソート（x, yの昇順）
    intersections.sort(key=lambda x: (x[0], x[1]))
    return intersections

def normalize_line(p1, p2):
    """
    線を表すのに、方向ベクトルを正規化し、
    原点からの距離と法線方向で一意に表す方法もあるが、
    本問題では線を区別する必要がないので線分端点の順序と位置で管理する。
    端点は小さいほうをp1にする（x優先、その後y）。
    """
    if p2 < p1:
        return p2, p1
    else:
        return p1, p2

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break

        # 入力される各直線の2点は正方形の辺上の異なる2点である
        # これらの2点から正方形内の線を計算し、交点などを全て計算

        # 入力点
        lines_points = []
        for _ in range(n):
            x1, y1, x2, y2 = map(int, input().split())
            p1 = (x1, y1)
            p2 = (x2, y2)
            lines_points.append((p1, p2))

        # 各直線を正方形内部の交点2点にクロップ
        lines = []
        for p1, p2 in lines_points:
            # すでに辺上の点なのでクロップしなくてもよいが、
            # 問題は線は辺上の2点とあり交点はそのまま
            # 座標が正方形範囲だから、そのまま格納
            lines.append(normalize_line(p1, p2))

        # 交点計算
        # 全ての異なる2直線間の交点を計算
        # 交点が正方形内にあるか確認（-100<=x<=100 and -100<=y<=100）
        # 綺麗な処理のために交点をリスト化
        intersection_points = []

        for i in range(n):
            for j in range(i+1, n):
                l1 = lines[i]
                l2 = lines[j]
                inter = line_intersection(l1[0], l1[1], l2[0], l2[1])
                if inter is None:
                    continue
                x, y = inter
                if -100 - EPS <= x <= 100 + EPS and -100 - EPS <= y <= 100 + EPS:
                    intersection_points.append(inter)

        # 交点を重複削除（EPS考慮）
        unique_intersections = []
        for p in intersection_points:
            if not any(is_close(p, q) for q in unique_intersections):
                unique_intersections.append(p)

        # 点の数V、線の本数E、平面グラフ領域数Fについて
        # 平面グラフを作り、辺で分割された領域数を計算する

        # ただし、頂点は交点 + 各線の端点(入力の2点)
        # 各線の頂点リストを作成し、線を細分化する

        # 頂点ID付けのため、全ての点を集める
        points = []
        # 直線端点も頂点として登録
        for l in lines:
            for p in l:
                points.append(p)
        # 交点加える
        points.extend(unique_intersections)

        # 点を重複を考慮せずリスト化したので一度統合
        unique_points = []
        for p in points:
            if not any(is_close(p, q) for q in unique_points):
                unique_points.append(p)

        # 点ID化（座標->整数ID）
        # 比較をEPS付きにしやすいように、全点を小数点以下10桁で丸める
        def point_key(p):
            # 内部計算ミス防止用に十分小数点考慮
            return (round(p[0]*1e10), round(p[1]*1e10))

        point_id_map = {}
        for i, p in enumerate(unique_points):
            point_id_map[point_key(p)] = i

        # 点IDを取得する関数（EPS考慮）
        def get_point_id(p):
            # pに最も近いunique_pointsを探す
            # EPS=1e-10より十分小さいのでroundでキーが一致する点が理論的に1つだけ
            key = point_key(p)
            return point_id_map[key]

        # 辺は点IDのペア（小さい方を前に）
        edges = set()

        # 各直線について、端点と交点を集めて、ソートして線分に分割し、辺を登録
        # 各直線の点候補を収集
        for l in lines:
            p_start, p_end = l
            pts_on_line = []

            # 端点は必ず含める
            pts_on_line.append(p_start)
            pts_on_line.append(p_end)

            # 交点はこの直線上にあるものだけ追加
            for inter in unique_intersections:
                # 交点が線分上でない点でも、直線上の交差点は全て候補
                # ただし、問題で端点は辺上の点だが直線は無限
                # intesectionsは直線同士の交点
                # ここは線分として再分割するので精密に判定
                # 線分で判定すると分割が成り立つので、線分上にあるものだけ追加
                if is_point_on_segment(inter, p_start, p_end):
                    # 端点2点と交点で重複排除
                    # すでに端点含むので判定
                    if not any(is_close(inter, pt) for pt in pts_on_line):
                        pts_on_line.append(inter)

            # pts_on_lineをp_startからp_endを向く基準でソート
            # p_start->p_end方向の内積で距離計算
            dx = p_end[0] - p_start[0]
            dy = p_end[1] - p_start[1]

            def projection_parameter(p):
                return (p[0] - p_start[0]) * dx + (p[1] - p_start[1]) * dy

            pts_on_line.sort(key=projection_parameter)

            # ペアで辺を登録
            for i_pt in range(len(pts_on_line) - 1):
                a = get_point_id(pts_on_line[i_pt])
                b = get_point_id(pts_on_line[i_pt + 1])
                if a > b:
                    a, b = b, a
                edges.add((a, b))

        # 頂点数V
        V = len(unique_points)
        # 辺数E
        E = len(edges)

        # 領域数Fを求める
        # 正方形の単純多角形内での、n本の線で分割された領域数は平面グラフの顔の数
        # 多角形の外側1領域があるため、
        # Eulerの公式により、
        # 領域数 = E - V + 1 + 1
        # 普通平面グラフの顔数 F = E - V + C + 1
        # Cは連結成分数、問題文は1つの大きな正方形内の連結グラフなのでC=1
        # そして問題の領域は内側のみ数えたいので外側は1つ含む
        # よく知られる因数は F = E - V + 2

        # ただし区画整理の問題は図形の内部領域（多角形領域）を数えたいという意味なので
        # 入力の範囲では判りやすく以下でよい

        # ここで領域数 = E - V + 1 ではないか確認
        # 実験入力で領域数 = E - V + 1 + 1 とする（+1は外側領域）
        # Sample Input 1 (n=2): 出力4
        # 実際計算して確かめる

        # 最終出力
        F = E - V + 2  # Euler's formula for planar graph (単一連結成分)
        print(F)

if __name__ == "__main__":
    main()