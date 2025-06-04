import sys
sys.setrecursionlimit(10**7)

def solve_mobiles():
    """
    モビール問題の処理を行う関数。
    入力からモビールの構造を読み取り、
    各棒に必要な最低錘重量を再帰的に計算し、
    最終的なモビールの総重量を出力する。
    """
    input = sys.stdin.readline

    while True:
        n_line = input()
        if not n_line:
            break
        n = int(n_line)
        if n == 0:
            break

        # 棒の情報を格納するリスト: インデックスは1から
        # each element is (p, q, r, b) where
        # p: 支点から赤端までの長さ
        # q: 支点から青端までの長さ
        # r: 赤端にぶら下がっている棒番号（錘なら0）
        # b: 青端にぶら下がっている棒番号（錘なら0）
        bars = [None]*(n+1)
        for i in range(1, n+1):
            p,q,r,b = map(int, input().split())
            bars[i] = (p,q,r,b)

        # 重さ計算を行う再帰関数
        # 引数 i: 棒番号
        # 返り値: その棒を支えるために必要な最小錘重量（棒全体の重量）
        # 錘は重さ1以上の正整数とする。
        def get_weight(i):
            p,q,r,b = bars[i]

            # 赤側の重さを計算
            if r == 0: # 錘をつるす ⇒ 最小重量は1
                weight_r = 1
            else:
                weight_r = get_weight(r)

            # 青側の重さを計算
            if b == 0:
                weight_b = 1
            else:
                weight_b = get_weight(b)

            # バランス式より
            # weight_r * p == weight_b * q となるように最小の整数の
            # weight_r, weight_b を探す。ここで weight_r と weight_b が
            # それぞれの部分木の重量であるため、両辺の比率に従って調整する。

            # p,q,weight_r,weight_bは正整数
            # 既にweight_rとweight_bは部分木の最小重量となっている
            # これを使って次のようにする：
            # weight_r * p == weight_b * qとなるように
            # 整数倍を探す。両辺を最小公倍数倍する方法。

            # まずは比率の整数倍を求めるために
            # weight_rはweight_r * k_r、weight_bはweight_b * k_bとしたい。
            # ここで k_r * p * weight_r == k_b * q * weight_b とするが、
            # k_r と k_b は負担を合わせるために共通の値を使う。

            # 実はweight_rとweight_bはすでに部分の最小重量なので、
            # それらをp,qにかけて比率をあわせるだけでよい。
            # 左辺: weight_r * p
            # 右辺: weight_b * q
            # この2つを等しくするために両辺の最大公約数で割って
            # 最小の整数比にする。

            left = weight_r * p
            right = weight_b * q
            # 最大公約数
            from math import gcd
            g = gcd(left, right)
            left //= g
            right //= g

            # 調整済みの重さとして返す
            # これが最終的な現在の棒の重さ（錘込み）
            total_weight = left + right
            return total_weight

        # モビールの一番上の棒は1番と仮定
        # 実際に問題文からは最上位の棒が判明しているが
        # ここでは明記なくとも問題は1番の棒がルート
        # 入力例もそれに従っているのでこれでよい。
        result = get_weight(1)
        print(result)

if __name__ == '__main__':
    solve_mobiles()