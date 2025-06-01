# 人生ゲームの期待値を求めるプログラム
# 入力の複数データセットに対して、ゴール時の所持金の期待値を計算し、小数点以下切り捨てで出力する

import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline

    while True:
        # 入力：ルーレットの区分数X、マス目の数Y、イベントマスの数Z
        X, Y, Z = map(int, input().split())
        if X == 0 and Y == 0 and Z == 0:
            break

        # ルーレットの値リスト V1 ... VX
        roulette = list(map(int, input().split()))
        # イベントマス情報（辞書形式でマス番号→(イベント種類, 値)）
        events = dict()
        for _ in range(Z):
            N_i, E_i, A_i = map(int, input().split())
            events[N_i] = (E_i, A_i)

        # 期待値DPテーブル: dp[pos][money] 状態は
        # pos: 現在位置（マス番号0～Y）
        # money: 現在の所持金 　　 ただし範囲が無限になりうるため直接管理できないので工夫が必要
        # → 所持金は0以上、増減量最大100なので、敷居を設けずに状態保持は困難
        # → 所持金は0からの変動のみ。だが巨大なDPは無理。期待値DPでは、所持金を状態に含めると大変
        #
        # よって期待値DPを状態を位置だけにして計算する必要がある。
        # なぜなら、所持金は過去のイベントで変わるが、
        # イベント後はイベントの追加イベントがない（イベントのイベントは無視）ので、
        # 各マスでの期待値を求めれば良い。
        #
        # アルゴリズム：
        # dp[pos] := ゴールにたどり着くまでに、その位置から得られる所持金の期待値
        # ゴールY以上の位置にたどり着いたらそこからゴールなので期待値は0

        # イベントを考慮するヘルパー関数
        def after_event(pos, money):
            # posはイベントマスの位置、money現在の所持金
            # eventは1つだけ（重ならない）
            E_A = events.get(pos)
            if not E_A:
                return pos, money
            E_i, A_i = E_A
            if E_i == 1:
                # posからA_iマス先に進む。イベントのイベントは無視する
                new_pos = pos + A_i
                if new_pos > Y:
                    new_pos = Y
                return new_pos, money
            elif E_i == 2:
                # 指定値A_iの金額を得る
                new_money = money + A_i
                return pos, new_money
            else:
                # 指定値A_iの金額を支払う
                new_money = money - A_i
                if new_money < 0:
                    new_money = 0
                return pos, new_money

        # dp[pos]: その位置からゴールまでの期待値
        dp = [-1.0] * (Y + 1)

        def dfs(pos):
            if pos >= Y:
                # ゴール到達: 所持金期待値は0（ここから先はイベントなし）
                return 0.0
            if dp[pos] >= 0:
                return dp[pos]

            exp_val = 0.0
            num = len(roulette)
            prob = 1.0 / num

            for roll in roulette:
                next_pos = pos + roll
                if next_pos > Y:
                    next_pos = Y
                # next_posに止まった時のイベント処理
                # このイベントは通過ではなく止まった時のみ発生
                # イベントのイベントは発生しない
                ne_pos, ne_money = after_event(next_pos, 0)
                # ne_moneyは変化分なので、初期0に対する増減値
                # 今回のdpはposからの期待値でmoney0からの変化値の期待値を計算するので、
                # ne_moneyは期待値に加算
                # ne_posからの期待値を再帰的に求める
                exp_val += prob * (ne_money + dfs(ne_pos))

            dp[pos] = exp_val
            return exp_val

        # 初期位置0からスタート、所持金0なので期待値はdfs(0)
        ans = dfs(0)

        # 出力は切り捨ての整数
        print(int(ans))


if __name__ == '__main__':
    main()