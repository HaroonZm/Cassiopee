# 解法の概要
# スパゲッティの理想の茹で時間は T 秒で、誤差 E 秒以内であれば良いとする。
# つまり、計測したい時間は [T-E, T+E] の範囲内の整数秒である。
# 各砂時計 i は xi 秒を1単位として、それの倍数の時間を計測できる。
# したがって、xi の倍数のいずれかが [T-E, T+E] の範囲に入るかを確認すればよい。
#
# 処理手順：
# 1. 入力として N, T, E, と砂時計の時間リストを受け取る
# 2. 各砂時計 xi について、k = 1,2,...として k*xi が T+E 以下の間繰り返す
# 3. k*xi が T-E 以上かつ T+E 以下なら、その砂時計は条件を満たす
# 4. 最初に条件を満たした砂時計のインデックス (1-based) を出力する
# 5. どの砂時計も条件を満たさなければ -1 を出力する
#
# 制約が小さいため、この方法は十分高速である。

def main():
    import sys
    input = sys.stdin.readline

    N, T, E = map(int, input().split())
    x = list(map(int, input().split()))

    lower = T - E
    upper = T + E

    for i in range(N):
        xi = x[i]
        # kを1からスタートして、k * xi <= upper まで繰り返し
        k = 1
        while k * xi <= upper:
            time = k * xi
            if lower <= time <= upper:
                print(i + 1)
                return
            k += 1
    # 条件を満たす砂時計がなければ -1 を出力
    print(-1)

if __name__ == "__main__":
    main()