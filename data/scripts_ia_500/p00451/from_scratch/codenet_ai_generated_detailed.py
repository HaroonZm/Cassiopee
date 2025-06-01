import sys

def longest_common_substring(s1: str, s2: str) -> int:
    """
    この関数は、2つの文字列 s1 と s2 の最長共通部分文字列の長さを求める。
    動的計画法を用いることで、計算量 O(len(s1)*len(s2)) となる。

    アプローチ:
    - dp[i][j] を s1 の i-1 文字目までと s2 の j-1 文字目までの文字列の最長共通部分文字列の長さ（末尾位置が i-1, j-1 にあるもの）と定義する。
    - dp[i][j] は s1[i-1] == s2[j-1] の場合 dp[i-1][j-1] + 1、それ以外は 0。
    - これを s1, s2 の全組み合わせで計算し、最大値を保持する。

    パフォーマンス向上のために列方向の dp を1次元リストで管理する。
    """
    len_s1 = len(s1)
    len_s2 = len(s2)

    # dpの初期化。dp[j] は s1 の i-1 文字目までと s2 の j-1 文字目までの最長共通部分文字列の長さを保持
    dp = [0] * (len_s2 + 1)
    max_length = 0

    for i in range(1, len_s1 + 1):
        # dp_temp は今回の i に対応する dp の結果を一時保管する
        dp_temp = [0] * (len_s2 + 1)
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                # 文字が一致した場合、左上の値に1を足す
                dp_temp[j] = dp[j - 1] + 1
                if dp_temp[j] > max_length:
                    max_length = dp_temp[j]
            else:
                dp_temp[j] = 0
        dp = dp_temp

    return max_length

def main():
    # 入力は複数のデータセットが EOF まで続くため、EOFまで繰り返し処理する
    input_lines = sys.stdin.read().strip().split('\n')
    # 2行ずつ読み込むためにループ
    for i in range(0, len(input_lines), 2):
        s1 = input_lines[i].rstrip('\r\n')
        s2 = input_lines[i+1].rstrip('\r\n')
        # 最長共通部分文字列の長さを計算し出力
        print(longest_common_substring(s1, s2))

if __name__ == "__main__":
    main()