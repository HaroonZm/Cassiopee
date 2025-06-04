import sys
import math

# 小数点以下の許容誤差
EPS = 1e-9

# 2点が非常に近いか判定
def nearly_equal(a, b):
    return abs(a - b) <= EPS

# 2点間の距離
def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

# 線分p1-p2とq1-q2の交差判定と交点計算
# 交差すれば(交差点のx, y), True を返し、交差しなければ(None, None), Falseを返す
def segment_intersection(p1, p2, q1, q2):
    # 線分の各ベクトル
    dx1 = p2[0] - p1[0]
    dy1 = p2[1] - p1[1]
    dx2 = q2[0] - q1[0]
    dy2 = q2[1] - q1[1]

    # 2線分の連立方程式の判別式
    det = dx1 * dy2 - dy1 * dx2
    if nearly_equal(det, 0):
        return (None, None), False  # 平行または同一直線上

    # t, uを計算し、線分のパラメータ範囲内か確認
    t = ((q1[0] - p1[0]) * dy2 - (q1[1] - p1[1]) * dx2) / det
    u = ((q1[0] - p1[0]) * dy1 - (q1[1] - p1[1]) * dx1) / det

    if -EPS <= t <= 1 + EPS and -EPS <= u <= 1 + EPS:
        # 交点座標
        x = p1[0] + t * dx1
        y = p1[1] + t * dy1
        return (x, y), True
    return (None, None), False

# 2点座標が同一点か判定
def point_equal(p, q):
    return dist(p, q) <= EPS

def solve():
    input = sys.stdin.readline
    T = int(input())  # データセットの数

    for _ in range(T):
        # A, Bの座標
        xa, ya = map(float, input().split())
        xb, yb = map(float, input().split())
        A = (xa, ya)
        B = (xb, yb)

        n = int(input())
        # 既存路線情報:
        # 各要素は (開始点, 終点, 所有者(o), 高架or地下(l))
        routes = []
        for __ in range(n):
            xs, ys, xt, yt, o, l = input().split()
            xs = float(xs)
            ys = float(ys)
            xt = float(xt)
            yt = float(yt)
            o = int(o)
            l = int(l)
            routes.append(((xs, ys), (xt, yt), o, l))

        # 新路線はA-Bを結ぶ線分
        new_start, new_end = A, B

        # 新路線と既存路線の交点を全て求める
        # 交点座標とその交差路線の情報(所有者o,l)を管理する
        intersections = []

        for (s, t, o, l) in routes:
            P, intersect = segment_intersection(new_start, new_end, s, t)
            if intersect:
                intersections.append((P, o, l))

        # 交点が無ければ新線は単に高架か地下のどちらかで済むので出入口なし
        if len(intersections) == 0:
            print(0)
            continue

        # 交点の位置に基づき線分を分割するため、
        # AからBに向かう順で交点をソート
        # Aからの距離を計算し、それでソート
        def dist_from_A(p):
            return math.hypot(p[0] - A[0], p[1] - A[1])

        intersections.sort(key=lambda x: dist_from_A(x[0]))

        # 新線の区間は n_intersections+1 個に分かれる
        # それぞれの区間の線路は高架(1)か地下(0)かを決める
        # 各交点で新線の線路状態が決まる:
        # 自社所有路線と交差 => 新線は既存路線と同じ(乗換利便性向上)
        # 他社所有路線と交差 => 新線は既存路線と逆(妨害回避)
        # 複数交点で所有者が異なる場合は条件付きで決めていく必要あり

        # モデル化：
        # 新線の各区間を0(地下),1(高架)どちらかの状態で持つ
        # 交点では既存路線とのルールにより状態が強制される

        # まずは交点ごとに交点状態の制約を作る
        # 交点での制約は：
        # 新線の状態 s_i = 既存線路状態 l (自社所有なら)
        # s_i = 1 - l (他社所有なら)
        # ここでs_iは交点の1つ左区間の状態=右区間の状態。つまり交点自体の状態。
        # 実際には新線は各区間に状態を持つので、区間i, i+1をまたぐ交点では左区間or右区間の状態を決める必要アリ。

        # 区間数 = len(intersections)+1
        m = len(intersections) + 1

        # 各区間は0または1の状態

        # 交点は区間の境界にあるため、
        # 交点iは区間iと区間i+1の間にあると考える

        # 問題：
        # 交点iでの新線の状態 s は
        # 自社路線なら s_i == l_i
        # 他社路線なら s_i != l_i

        # ここで、s_iは交点との接点での状態。
        # つまり、交点iの左区間の状態 or 右区間の状態で
        # 状態が変わることは出入口に相当する

        # 線路の状態切替(出入口)の個数は
        # 隣り合う区間の状態が異なる回数

        # A,Bはどちらの状態でもよいので、全探索orDPで最小化する

        # 方針：
        # 区間iは0か1を取る
        # 交点i (i=0...m-2) において
        # 状態 s must satisfy
        # 条件は s[i] or s[i+1]のいずれかが交点の条件を満たす
        # つまり、交点条件は交点での新線の状態＝

        # ここでは便宜上、交点の状態 = 区間iの状態（左側区間）
        # と定める。

        # 交点iの条件は、区間iの状態が
        # 自社路線　　　: s[i] == l_i
        # 他社路線　　　: s[i] == 1 - l_i

        # これで決める。ただし端点のA,Bに状態制約なし。

        # まとめる:
        # - 区間i (0<=i<m-1) に交点iの条件あり
        # - 区間m-1 は交点なし

        # 交点iごとの条件が区間iの状態を決める

        # 状態割り当ての矛盾があれば解なしだが、
        # 問題文により解ありと仮定

        # 以上より、
        # 区間iは強制的に状態を決められる
        # 標準的な区間の状態は
        # s[i] = l_i (自社路線)
        # s[i] = 1 - l_i (他社路線)
        # 条件が重複するなら矛盾？

        # では例えば複数の交点がある時どうなる？
        # 交点があるたびに区間の状態変えられないので、
        # 交点iごとに区間iの状態は決定される

        # しかし区間iの状態が交点毎に違う指示を受ける可能性はない
        # 交点iは区間iの状態だけ指示するのでOK

        # では区間m-1については交点制約なしなので状態自由に選んでよい

        # 状態の決定:
        # 区間0～m-2: 交点iの指定で状態1つに決定
        # 区間m-1: 自由に0か1選べる

        # これで状態を確定

        # 出入口数は隣接区間の状態が異なる数

        # m-1区間境界のうち、m-2は交点境界
        # 末尾の境界は最後の区間>なし交点境界。ここでは何もない

        # 区間m-1の状態は0か1どちらかを選べる

        # よって状態パターンは2通りしかない：
        # 区間m-1 = 0
        # 区間m-1 = 1

        # それぞれで全部の区間状態を決めて
        # 出入口数を計算し、最小を答える

        # 実装開始

        # まず交点iの状態（左区間i）を設定
        fixed_states = []
        for (p, o, l) in intersections:
            if o == 1:
                fixed_states.append(l)      # 自社路線の場合は同じ状態
            else:
                fixed_states.append(1 - l)  # 他社路線の場合は逆の状態

        # 交点数 = len(fixed_states) = m - 1

        min_gate = None

        # 区間m-1 の状態0または1で試す
        for last_state in [0, 1]:
            states = fixed_states[:] + [last_state]

            # 出入口(状態遷移)個数を数える
            gates = 0
            for i in range(m - 1):
                if states[i] != states[i + 1]:
                    gates += 1

            if min_gate is None or gates < min_gate:
                min_gate = gates

        # 答えを出力
        print(min_gate)


if __name__ == "__main__":
    solve()