# 問題概要：
# n 分間のトンネル調査で、各分の入口と出口の通過車数が与えられる。
# 時刻 j 分（j=0～n）におけるトンネル内の車の台数 S_j を計算し、その最大値を求める。
# 途中で S_j が負になることがあれば、「エラー」として 0 を出力する。

# 入力例
# n (調査時間)
# m (調査開始時のトンネル内車両数)
# n 行の「入口を通過した車の台数」「出口を通過した車の台数」

# 方針：
# ・S_0 = m
# ・S_j = S_{j-1} + 入口通過車数 - 出口通過車数
# ・どの時点でも S_j < 0 なら 0 を出力
# ・それ以外は max(S_j) を出力

# 以下に詳細コメント付きで実装。

def main():
    import sys

    # 入力を読み込む
    n = int(sys.stdin.readline())   # 調査時間（分）
    m = int(sys.stdin.readline())   # 調査開始時のトンネル内車両数

    # S_j の計算と管理
    S = m  # 現在のトンネル内の車両数、初期値は m
    max_S = S  # 最大値を記録

    for _ in range(n):
        # 入口と出口の車の台数を読み込み
        enter, exit = map(int, sys.stdin.readline().split())
        
        # 車両数更新
        S = S + enter - exit
        
        # 負になるかチェック：負ならエラーの意味で 0 を出力して終了
        if S < 0:
            print(0)
            return
        
        # 最大値の更新
        if S > max_S:
            max_S = S

    # 最終的に最大値を出力
    print(max_S)

if __name__ == "__main__":
    main()