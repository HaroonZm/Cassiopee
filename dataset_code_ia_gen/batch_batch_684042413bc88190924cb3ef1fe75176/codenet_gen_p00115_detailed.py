import sys

def vector_sub(a, b):
    """座標ベクトルaからbを引く（a - b）"""
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

def vector_dot(a, b):
    """ベクトルaとbの内積"""
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def vector_cross(a, b):
    """ベクトルaとbの外積"""
    return (a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0])

def point_in_triangle(p, a, b, c):
    """
    点pが三角形abcの内部または境界にあるか判定
    重心座標を使った判定法（境界を含む判定）
    """
    v0 = vector_sub(c, a)
    v1 = vector_sub(b, a)
    v2 = vector_sub(p, a)
    dot00 = vector_dot(v0, v0)
    dot01 = vector_dot(v0, v1)
    dot02 = vector_dot(v0, v2)
    dot11 = vector_dot(v1, v1)
    dot12 = vector_dot(v1, v2)

    denom = dot00 * dot11 - dot01 * dot01
    if denom == 0:
        # 三角形が退化している（問題文では想定外）
        return False
    inv_denom = 1 / denom
    u = (dot11 * dot02 - dot01 * dot12) * inv_denom
    v = (dot00 * dot12 - dot01 * dot02) * inv_denom

    # u,v >=0 かつ u+v <=1 なら三角形内部または辺上
    return (u >= -1e-10) and (v >= -1e-10) and (u + v <= 1 + 1e-10)

def point_in_plane(p, a, b, c):
    """
    点pが三角形abcと同一平面上かどうかを判定
    この後の判定とセットで使うため単独での使用は少ないが、
    平面距離が0に近い場合に True を返す。
    """
    # 平面の法線ベクトル
    ab = vector_sub(b, a)
    ac = vector_sub(c, a)
    normal = vector_cross(ab, ac)
    # 点pからaまでのベクトル
    ap = vector_sub(p, a)
    # 평面式の評価値
    # abs(normal・ap)が0に近ければpは平面上
    distance = abs(vector_dot(normal, ap))
    return distance < 1e-10

def segment_intersect_triangle(p0, p1, a, b, c):
    """
    線分 p0-p1 が三角形 abc に当たるか判定
    手順：
    1. 三角形の面の平面と線分の交点を求める
    2. 交点が線分内にあるか
    3. 交点が三角形内部にあるか

    境界は含む（＝交点が三角形の頂点や辺上でも当たる）
    """
    ab = vector_sub(b, a)
    ac = vector_sub(c, a)
    normal = vector_cross(ab, ac)
    # 線分方向ベクトル
    dir_vec = vector_sub(p1, p0)
    denom = vector_dot(normal, dir_vec)
    if abs(denom) < 1e-15:
        # 線分は三角形面と平行（交点なし、または線分が面に完全にのっている）
        # 問題文に線分が三角形の辺や頂点の方向に潰れて見えるものはないとあるので、
        # この場合は交点なしとして扱う
        return False
    t = vector_dot(normal, vector_sub(a, p0)) / denom
    if t < -1e-12 or t > 1 + 1e-12:
        # 交点は線分の外（拡張線上）
        return False
    # 交点の座標
    intersect = (p0[0] + t*dir_vec[0], p0[1] + t*dir_vec[1], p0[2] + t*dir_vec[2])
    # 交点が三角形内部か判定
    return point_in_triangle(intersect, a, b, c)

def vector_length(v):
    """ベクトルの大きさ"""
    return (v[0]**2 + v[1]**2 + v[2]**2)**0.5

def is_point_in_tetrahedron(p, a, b, c, o):
    """
    敵点pが点o,a,b,cで囲まれた四面体内部にあるかを判定するのに使うことができるが、
    今回は敵点が三角形バリア内にある場合MISSなので、
    三角形内部で敵点を判定した後の判定は要らない。
    今回は利用しない。
    """
    pass

def main():
    # 入力を読み込み
    uaz = tuple(map(int, sys.stdin.readline().split()))
    enemy = tuple(map(int, sys.stdin.readline().split()))
    v1 = tuple(map(int, sys.stdin.readline().split()))
    v2 = tuple(map(int, sys.stdin.readline().split()))
    v3 = tuple(map(int, sys.stdin.readline().split()))

    # 1. 敵がバリア内にいる場合は "MISS"
    # バリアの平面上（厳密に計算） + バリア三角形内か？
    # 敵位置が三角形の面にあるか判定
    # ただし、この問題では「敵がバリア内にいる」は「敵位置が三角形内」と解釈する
    # 宇宙空間なので、バリアは面要素で、それ以外は空間なので内包判定は三角形面上のみでよい
    # 点が三角形平面上かは単に法線ベクトルとの内積距離で調べ、平面上なら内部判定する

    # まず敵がバリア面と同じ平面上にあるか
    if point_in_plane(enemy, v1, v2, v3):
        # 平面上なら三角形内部判定
        if point_in_triangle(enemy, v1, v2, v3):
            print("MISS")
            return

    # 2. ビームはUAZから敵へ直線上に発射
    # この線分がバリア三角形に当たるか判定
    # バリアはアドバンス号から三角形に見えるもののみ対象であるが
    # 問題文で「線分につぶれて見えるものはない」とあり、
    # 三角形が潰れてみえるものは扱わないので特別な判定不要

    hit_barrier = segment_intersect_triangle(uaz, enemy, v1, v2, v3)
    if hit_barrier:
        print("MISS")
        return

    # 3. 当たらなければ "HIT"
    print("HIT")

if __name__ == "__main__":
    main()