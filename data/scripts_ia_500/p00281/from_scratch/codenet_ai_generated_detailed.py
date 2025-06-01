# 親方の給料計算プログラム
# N: 職人の数
# M: 工事の種類の数
# a: 職人iが工事jをこなした回数を記録（辞書形式で効率よく管理）
# L: 給料の計算回数
# b: 各回の工事単価リスト
#
# 入力の仕様：
# まず N, M
# 次に職人、工事の種類、回数（s, t, e）が0 0 0で終了
# 次にL
# L回分の単価情報
#
# 出力の仕様：
# L回分、各回の各職人の給料を空白区切りで出力

import sys
input = sys.stdin.readline

def main():
    # N: 職人数, M: 工事種類数
    N, M = map(int, input().split())

    # 職人がこなした工事記録を格納
    # 各職人ごとに {工事種類: 回数} の辞書を保持
    # 大きなNとMなのでメモリ節約は辞書の使用が適している
    work_counts = [{} for _ in range(N)]

    # 作業記録の入力読み込み
    while True:
        s, t, e = map(int, input().split())
        if s == 0 and t == 0 and e == 0:
            break
        # 0-origin に変換して格納
        work_counts[s-1][t-1] = e

    L = int(input())  # 給料算出回数

    # 各回の単価入力
    # b_list[l] = 各工事jの単価のリスト
    b_list = [list(map(int, input().split())) for _ in range(L)]

    # 各給料計算の結果を格納していく
    # 出力のフォーマットに注意して最後にまとめて出力
    for l in range(L):
        b = b_list[l]
        # 職人ごとの給料計算
        salaries = [0]*N
        # 計算量削減のため、職人ごとに回数がある工事だけ計算する
        for i in range(N):
            total = 0
            for job_type, count in work_counts[i].items():
                total += b[job_type] * count
            salaries[i] = total
        print(*salaries)

if __name__ == "__main__":
    main()