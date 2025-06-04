import sys

def is_left_of(p, x0, y0, x1, y1):
    # 判定点pが直線(x0,y0)-(x1,y1)の左側にあるかどうかを判定する
    # ここで左側は、(x1 - x0, y1 - y0)から見て反時計回りの方向を指す
    return (x1 - x0) * (p[1] - y0) - (y1 - y0) * (p[0] - x0) > 0

def count_strawberries_side(strawberries, x0, y0, x1, y1):
    # 直線(x0,y0)-(x1,y1)の左側にあるイチゴの個数を返す
    count = 0
    for p in strawberries:
        if is_left_of(p, x0, y0, x1, y1):
            count += 1
    return count

def solve():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        W, H, N = map(int, line.split())
        if W == 0 and H == 0 and N == 0:
            break
        
        strawberries = []
        for _ in range(2 * N):
            x, y = map(int, input().split())
            strawberries.append((x,y))
        
        total_count = 0  # 条件を満たす線分の組み合わせ数
        
        # イコの包丁の端点は左辺(0,0)-(0,H)上にあるので、y座標は0～Hの間で離散的な2N+1ポイントを考慮する
        # ピコの包丁の端点は右辺(W,0)-(W,H)上にある同様
        # しかし問題では「包丁を置く点は辺上の任意の点を選べ、それぞれの点は一様確率で選ばれる」
        # よって考慮すべきは、イチゴのy座標の区間での位置関係のみ。
        #
        # 解決策：
        # イチゴは有限個であり、2N個
        # 左辺上の点と右辺上の点の組み合わせは、yが連続値で無限にあるので、
        # イチゴのy座標に注目し、y位置でのイチゴの位置関係が変化する区間のみ考え、
        # イチゴの取り分が変わるのはその分割線がある位置のy範囲で変わる
        #
        # よって、イチゴのy座標の集合と0,Hを合わせてソートし、それらのy間隔で-それぞれで直線の下端点上で起こる分割結果は一定
        #
        # これを利用して、離散的に検討可能とし、イコの端点yをイチゴのy座標群+0,Hで分割し、
        # 同様にピコの端点yも同様に分割すれば、有限個の候補で、総計O((2N+2)^2)候補で判定可能
        
        # 左辺の候補y座標セット（0,Hとイチゴのy座標を追加）
        left_candidates = set([0,H])
        # 右辺の候補y座標セット（0,Hとイチゴのy座標を追加）
        right_candidates = set([0,H])
        for x,y in strawberries:
            if x == 0:
                left_candidates.add(y)
            if x == W:
                right_candidates.add(y)
        
        # 候補点をソートしてリスト化
        left_candidates = sorted(left_candidates)
        right_candidates = sorted(right_candidates)
        
        # あるy間の中間値を取るための補助関数
        def mid(a, b):
            return (a + b) / 2
        
        # それぞれの区間で中点を取って判定するためのy候補リスト作成
        left_points = []
        for i in range(len(left_candidates) - 1):
            left_points.append(mid(left_candidates[i], left_candidates[i+1]))
        # 端点も候補として含める
        left_points += left_candidates
        
        right_points = []
        for i in range(len(right_candidates) - 1):
            right_points.append(mid(right_candidates[i], right_candidates[i+1]))
        right_points += right_candidates
        
        # 上端座標(0, y_left)、(W,y_right) で切断線を引く。全組み合わせを調べる
        # 二次元的に考えるが、個数はmaxで(2N+2)程度なので約200*200=40000で許容範囲。
        
        def cut_line_ends(y_left, y_right):
            # 包丁の端点は(0,y_left)と(W,y_right)
            # この直線で切断して左側に何個のイチゴがあるか数える
            left_count = 0
            for x,y in strawberries:
                # 点が線の左側（包丁の左側）にあるか
                # 左側をis_left_of関数で判定
                if is_left_of((x,y), 0, y_left, W, y_right):
                    left_count += 1
            return left_count
        
        total = len(left_points) * len(right_points)
        valid = 0
        
        for yl in left_points:
            if yl < 0 or yl > H:
                continue
            for yr in right_points:
                if yr < 0 or yr > H:
                    continue
                cnt_left = cut_line_ends(yl, yr)
                # イチゴは2N個、ちょうどN個ずつに分けたいので左部分にN個
                if cnt_left == N:
                    valid += 1
        
        ans = valid / total if total > 0 else 0.0
        print("%.10f" % ans)

if __name__ == "__main__":
    solve()