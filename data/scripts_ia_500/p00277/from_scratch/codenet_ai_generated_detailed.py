import sys
import bisect

def main():
    input = sys.stdin.readline
    N, R, L = map(int, input().split())

    # 得点を保持する配列、初期はすべて0点
    scores = [0]*(N+1)

    # ログ記録を読み取り（d_i, t_i, x_i）
    logs = []
    for _ in range(R):
        d, t, x = input().split()
        logs.append((int(d), int(t), int(x)))

    # 現在のトップチームを管理するための構造：
    # スコアとチームIDの組でソートされたリスト
    # スコアは昇順で、同じスコアならチームID昇順
    # これによりリスト[-1]が最大スコアかつID最小のチームを指す
    score_team_list = []
    for i in range(1, N+1):
        # スコア0の全チームを追加
        score_team_list.append((0, i))
    score_team_list.sort()

    # チームの現在のスコアのindexを覚えるため辞書
    # （スコア, チームID）でindexを管理するのはコストが高いため
    # スコア更新時はバイナリサーチで探す
    # 各更新でリストから削除して挿入する操作はO(log N)
    def remove_team(score, team_id):
        # (score, team_id)の位置をバイナリサーチで探して削除
        idx = bisect.bisect_left(score_team_list, (score, team_id))
        score_team_list.pop(idx)

    def add_team(score, team_id):
        bisect.insort_left(score_team_list, (score, team_id))

    # コンテスト開始時点は0秒、トップはチームID1（スコア0の中でIDが最小）
    current_time = 0
    # 現在写っているチーム（初期は、スコア0でID最小のチーム=チーム1）
    # score_team_listは昇順なので最大は[-1]
    current_top_team = score_team_list[-1][1]
    # そのチームの映っている時間
    airtime = [0]*(N+1)

    for d, t, x in logs:
        # 現在のトップチームがテレビに映っていた時間を加算
        elapsed = t - current_time
        airtime[current_top_team] += elapsed

        # 現在のチームdのスコア更新処理
        old_score = scores[d]
        new_score = old_score + x
        scores[d] = new_score

        # リストから古い記録を削除、新しい記録を挿入
        remove_team(old_score, d)
        add_team(new_score, d)

        # トップチームを更新
        current_top_team = score_team_list[-1][1]
        current_time = t

    # 最後にコンテスト終了までトップチームの映っている時間を加算
    airtime[current_top_team] += (L - current_time)

    # 最大の映っていた時間を持つチームを探す
    max_time = max(airtime[1:])
    # 最も時間が長いチームIDのうち最小のものを出力
    for i in range(1, N+1):
        if airtime[i] == max_time:
            print(i)
            break

if __name__ == "__main__":
    main()