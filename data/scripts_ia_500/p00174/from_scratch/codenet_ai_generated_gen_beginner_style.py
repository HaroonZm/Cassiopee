while True:
    game1 = input()
    if game1 == "0":
        break
    game2 = input()
    game3 = input()

    games = [game1, game2, game3]

    # 初期サーブ権
    first_server = 'A'
    scores = []

    for game in games:
        score_A = 0
        score_B = 0
        # 1ゲーム目はAが最初のサーブ
        # 2,3ゲーム目は前のゲームの勝者が最初のサーブ

        # サーブを打った人の記録から得点を計算する
        # サーブを打った人＝その直前にポイントを取った人
        # なのでサーブした本人が最後にポイントを得ていると考えられる

        # まず最初のポイントは最初のサーブの人がポイントを取ったと仮定
        # しかし実際にはサーブした人がポイントを取ったため、最初のポイントは最初のサーブの人

        # したがって、1回目のサーブした人がポイントを取る
        # 2回目以降はサーブした人がポイントを取る

        # サーブの回数が0の可能性は問題文にないので無視

        # 最初のサーブ権からスタート
        # 1ゲーム目はfirst_serverは'A'
        # 2,3ゲーム目は直前ゲームの勝者に更新される

        # 1ゲーム目はfirst_serverは初期'A'
        # 2,3ゲーム目は前のゲームの勝者に更新済み

        # ゲーム中、サーブ順は記録されているので、これを使ってポイントを計算
        # 最初のポイントはサーブした人が取ったと考える

        # なので1文字目のサーブを打った人が最初に1点得る
        # 以降はサーブを打った人がポイントを得る

        # これで得点を計算し、11点先取か、10-10から2点差で決着する

        # 途中でゲーム終了時点の得点を知るため、得点判定を進める

        score_A = 0
        score_B = 0

        for i, server in enumerate(game):
            # サーブした人がポイントを取る
            if server == 'A':
                score_A += 1
            else:
                score_B += 1

            # 11点先取で勝利
            if (score_A >= 11 or score_B >= 11):
                # 10-10以降は2点差が必要
                if abs(score_A - score_B) >= 2:
                    break

        scores.append((score_A, score_B))

        # 次のゲームの最初のサーブはこのゲームの勝者
        if score_A > score_B:
            first_server = 'A'
        else:
            first_server = 'B'

    for s in scores:
        print(s[0], s[1])