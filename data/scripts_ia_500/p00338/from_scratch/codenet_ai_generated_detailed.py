import sys
import bisect

input = sys.stdin.readline

# 説明:
# - チームは1からNまで番号が振られている。
# - 全チームの初期得点は0。
# - 得点は更新命令で加算される。
# - 順位は得点の降順。得点が同じならチーム番号の昇順で決まる。
# - 「報告」命令では指定された順位mのチーム番号と得点を出力する。

# アプローチ:
# - 各チームの得点を保持する配列scoreを用意。
# - すべてのチームの初期データを(得点, チーム番号)で格納し、score_listに入れる。
# - score_listは (負の得点, チーム番号) の形にしておき、得点の高い順かつチーム番号の小さい順に並べる。
# - 更新命令ではチームの古いスコアをscore_listから削除し、新しいスコアを挿入する。
# - 挿入・削除はbisectで高速に行う（リストのソート順を維持する）。
# - 報告命令ではm-1番目の要素を取り出してチーム番号と得点を出力する。

# 注意点:
# - 更新は最大C回、各操作にO(log N)の操作を行うので、計算量は十分許容範囲内。
# - bisectで挿入・削除は O(log N) だが、削除は検索してからdelを行うので実質的には O(log N)。
# - 非常に大きい値の得点も対応可能（pは10^9まで）。

N, C = map(int, input().split())

# チームごとの得点管理
score = [0] * (N + 1)  # 1-indexedでチームのスコア

# 全チームの(負の得点, チーム番号)でリストを作成しソート
# こうすることで得点が高い順、得点が同じ場合はチーム番号の小さい順になる
score_list = [ (0, i) for i in range(1, N+1) ]
score_list.sort()

for _ in range(C):
    cmd = input().split()
    if cmd[0] == '0':
        # 更新命令
        t = int(cmd[1])
        p = int(cmd[2])
        old_score = score[t]
        new_score = old_score + p
        score[t] = new_score

        # 削除したい要素(負のold_score, t)をscore_listから探して削除
        # bisection で位置を特定する
        # 探すキーは (-old_score, t)
        key_old = (-old_score, t)
        pos = bisect.bisect_left(score_list, key_old)
        # posが見つかった位置
        del score_list[pos]

        # 新スコアの要素 (-new_score,t) を挿入
        key_new = (-new_score, t)
        bisect.insort_left(score_list, key_new)

    else:
        # 報告命令
        m = int(cmd[1])
        s, team_num = score_list[m - 1]
        # s は負の得点なので -s が得点
        print(team_num, -s)