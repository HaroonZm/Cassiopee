import sys
import bisect

def main():
    input = sys.stdin.readline
    N, C = map(int, input().split())

    # スコアはすべてのチームの初期点数を0に設定
    scores = [0] * (N + 1)

    # 現状の順位リストを作る
    # (スコアの降順, チーム番号の昇順) でソートした状態を維持するために、
    # (-score, team) の形で格納。スコアが大きいほど小さな負の数になるので
    # リストは昇順で保持し、bisectでの挿入を容易に。
    ranking = []
    for team in range(1, N + 1):
        ranking.append((0, team))
    ranking.sort()

    # チームごとの現在のランキング上の位置を管理
    # ランキング更新の際の削除用にindex参照が必要だが、
    # 単純なindex管理は難しいので、remove + bisectで再挿入する方式をとる。
    # removeは最悪O(N)だが、平均は高速化されるはず。

    for _ in range(C):
        command = input().split()
        if command[0] == '0':
            # 更新命令
            t = int(command[1])
            p = int(command[2])

            # 古いスコアの負の値でタプルを作成
            old_tuple = (-scores[t], t)
            # ランキングから古いスコアを削除
            # O(logN)のbisectで場所を探す
            idx = bisect.bisect_left(ranking, old_tuple)
            ranking.pop(idx)

            # スコア更新
            scores[t] += p

            # 新しいスコアの負の値でタプルを作成して挿入
            new_tuple = (-scores[t], t)
            bisect.insort_left(ranking, new_tuple)

        else:
            # 報告命令
            m = int(command[1])
            # mは1-indexなのでm-1でアクセス
            score, team = ranking[m-1]
            # rankingではスコアは負値なので復元して出力
            print(team, -score)

if __name__ == '__main__':
    main()