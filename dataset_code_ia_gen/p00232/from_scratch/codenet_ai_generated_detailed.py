import sys

sys.setrecursionlimit(10**7)

def main():
    while True:
        # 入力読み込み
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return
        X, Y, Z = map(int, line.split())
        if X == 0 and Y == 0 and Z == 0:
            break

        # ルーレットの値
        V = []
        while len(V) < X:
            line = sys.stdin.readline()
            if line == '':
                return
            V.extend(map(int, line.split()))
        V = V[:X]

        # イベント情報 (マス番号->(E, A))
        # スタート(0)とゴール(Y)はイベントなし
        events = dict()
        for _ in range(Z):
            while True:
                line = sys.stdin.readline()
                if line.strip() != '':
                    break
            Ni, Ei, Ai = map(int, line.strip().split())
            events[Ni] = (Ei, Ai)

        # 確率は均等
        p = 1 / X

        # DP用メモ化辞書： (pos, money) -> 期待値
        # ただしmoneyは0〜∞なので、そのまま状態に含めるのは爆発的に増える可能性あり
        # moneyは0以上で制約なしなので、メモ化はposだけで良いか？
        # 実はこの問題はposだけ状態としてDP可能
        # 理由：
        # - 所持金期待値にマルコフ性がある（現在位置のみで将来価値が決まる）
        # - 進んだ先のイベントは無視（イベントは1回だけ）
        #
        # よって期待値は位置だけの関数としてDP可能

        # DP[pos] = ゴールに到達した時の所持金の期待値（posからスタートして）
        DP = [-1] * (Y + 1)  # pos:0~Y. pos>Yはゴールとみなすのですぐに0

        # 位置０から開始、所持金0からスタート。状態はposのみなので期待値はそのまま保持
        # 期待値計算関数
        def expected(pos):
            # すでにゴールまたはゴールを超えている
            if pos >= Y:
                return 0.0

            if DP[pos] >= 0:
                return DP[pos]

            res = 0.0
            for v in V:
                next_pos = pos + v
                # ゴール到達判定
                if next_pos >= Y:
                    # ゴールを超えたらいくらでも所持金変わらず期待値は0
                    res += p * 0
                    continue

                # ゴールに達していなければイベント判定
                if next_pos in events:
                    E, A = events[next_pos]
                    if E == 1:
                        # 指定の値Aiだけ先へ進む(イベントは無視なので次のイベントなし)
                        next_pos2 = next_pos + A
                        if next_pos2 >= Y:
                            # ゴール到達
                            res += p * 0
                        else:
                            # イベント効果で位置だけ変更し、所持金変化なし
                            res += p * expected(next_pos2)
                    elif E == 2:
                        # 指定の値Aiの金額を得る
                        # ゴールではないので実際は期待値に直接加える
                        # 位置は変わらず次のターンはnext_posで続く
                        # ただしイベントの効果は1回のみ、次の期待値はnext_pos
                        # 期待値は得たお金＋残りゲームの期待値
                        # ただし進む先がイベントマスでも今回のイベント効果は1回だけで、
                        # 次のターンのイベントは普通に適用される（問題文の「イベントによって進んだ先のマスのイベントは無視します」は種類1のみの位置移動イベントの先のイベント無視のこと）
                        # ここは重要！このイベントは「そこに止まったことで起きるイベント」
                        # 「イベントによって進んだ先のマスのイベントは無視」というのは
                        # 種類1の「位置移動イベント」の以降のイベント無視に限定される
                        # 種類2,3は金銭変動だけで位置移動なしなので次のターンも普通にイベント判定される
                        sub = expected(next_pos)
                        res += p * (A + sub)
                    else:
                        # 指定の値Aiの金額を支払う
                        # 所持金は0未満にならない
                        # 同様に所持金期待値は (max(0, 保持金 - A)) + 次の期待値だが
                        # 所持金は期待値なのでmaxの処理は複雑
                        #
                        # 期待値的には max(0, current_money - A)は減用にできないが
                        # 所持金は0未満にならないルールより、支払う場合は所持金0以下に下げられない
                        #
                        # しかし現在の期待値は0→なのでもちろん最大マイナスA，0未満は0で切る
                        #
                        # 期待値 =期待値(次) + (所持金マイナスAだけ減少、最低0)
                        #
                        # 期待値の線形性のため、この分だけ差し引くだけでよいか？
                        #
                        # ここで、現在money=0なので max(0,0 - A)=0なので支払額のみ考慮すればよい
                        # 期待値計算のstateは所持金なしであり、マイナス効果はそのまま金額へマイナス期待値をかける
                        sub = expected(next_pos)
                        res += p * max(sub - A, 0)

                else:
                    # イベントなしマス
                    res += p * expected(next_pos)

            DP[pos] = res
            return res

        # スタートはpos=0、所持金0
        # 実はスタート地点はイベントなしなので普通にDP呼ぶだけ
        ans = expected(0)

        # 小数点以下切り捨て
        print(int(ans))


if __name__ == "__main__":
    main()