from __future__ import division, print_function

# Python 2とPython 3の互換性のために入力関数とrange関数を調整
try:
    input = raw_input  # Python 2ではraw_inputをinputに置き換え
    range = xrange     # Python 2ではxrangeをrangeに置き換え
except NameError:
    # Python 3ではraw_inputやxrangeは存在しないため何もしない
    pass

# 階段の段数ごとに必要な年数を計算するためのメモ化用リスト
a = [0] * 100

def solve(n):
    """
    指定された段数nに対して、一郎君がすべての上り方を実行するのに必要な日数（年数換算用）を計算する。

    再帰的に以下の関係で計算を行う:
    s(n) = s(n-3) + s(n-2) + s(n-1)
    ただし、初期条件は：
        s(1) = 1
        s(2) = 2
        s(3) = 4

    メモ化を用いて計算済みの値は再利用する。

    Args:
        n (int): 階段の段数（1以上の整数）

    Returns:
        int: n段階段の全ての上り方を実行するのに必要な日数
    """
    if n == 1:
        a[1] = 1
        return 1
    elif n == 2:
        a[2] = 2
        return 2
    elif n == 3:
        a[3] = 4
        return 4
    elif a[n] != 0:
        # 既に計算済みの場合はその値を返す
        return a[n]
    else:
        # 再帰呼び出しで計算しメモリに保存
        a[n] = solve(n - 3) + solve(n - 2) + solve(n - 1)
        return a[n]

def main():
    """
    標準入力から階段の段数を受け取り、0が入力されるまで繰り返し処理を行う。

    各入力値について、solve関数で必要な日数を計算し、それを3650日（10年相当）で割って年数換算し、
    1年分を加えた結果を出力する。

    入力が0の場合はプログラムを終了する。
    """
    while True:
        inp = int(input())  # ユーザーからの入力を整数として受け取る
        if inp == 0:
            # 0が入力されたら処理終了
            break
        # 日数を年数に換算し、結果を出力
        # //は整数除算、+1は切り上げ的な意味合い
        print(solve(inp) // 3650 + 1)

main()