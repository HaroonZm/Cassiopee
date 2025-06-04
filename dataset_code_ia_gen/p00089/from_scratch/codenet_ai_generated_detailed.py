import sys

# 読み込んだひし形のデータを解析し、最大和を求めるプログラム
# ひし形の形状は、上半分で幅が増え、下半分で幅が減る特徴があり、
# 各ステップは左下または右下に進むというルールに従う。

def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    n = len(lines)

    # 各行の整数リストに変換
    diamond = [list(map(int, line.split(','))) for line in lines]

    # 上半分(インデックス0から中間行まで)は要素数が1から増加
    # 下半分(中間行から最後)は要素数が減少する
    mid = (n + 1) // 2  # ひし形の中間行のインデックス(上半分の最大幅の行数)

    # dp配列はdiamondと同形状で、最大和を格納する
    # まずはdpをdiamondで初期化（深いコピーとして）
    dp = [row[:] for row in diamond]

    # 上半分の最大和を計算（トップダウンで）
    for i in range(1, mid):
        for j in range(len(diamond[i])):
            # 左下から来たか右下から来たかを判定
            # 左下はdp[i-1][j-1]（j-1>=0である場合）
            # 右下はdp[i-1][j]（j<len(dp[i-1])である場合）
            left_parent = dp[i-1][j-1] if j -1 >= 0 else -1
            right_parent = dp[i-1][j] if j < len(dp[i-1]) else -1
            dp[i][j] += max(left_parent, right_parent)

    # 下半分の最大和を計算（ボトムアップで）
    # 上半分の最下行(mid-1行目)はすでにdpに最大和が入っている
    for i in range(mid, n):
        for j in range(len(diamond[i])):
            # 上半分の拡大から逆に縮小するため、
            # dp[i][j] = diamond[i][j] + max(dp[i-1][j], dp[i-1][j+1])
            # j<len(dp[i-1]) かつ j+1 < len(dp[i-1]) の範囲内で比較
            left_parent = dp[i-1][j] if j < len(dp[i-1]) else -1
            right_parent = dp[i-1][j+1] if j+1 < len(dp[i-1]) else -1
            dp[i][j] += max(left_parent, right_parent)

    # 最終行の最大値が求める最大和
    print(max(dp[-1]))


if __name__ == "__main__":
    main()