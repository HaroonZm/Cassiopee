def max_electric_energy():
    import sys

    # 関数 calc_energy: 雄と雌のB粒子の差から放出エネルギーを計算
    def calc_energy(bm, bw):
        diff = abs(bm - bw)
        return diff * (diff - 30) * (diff - 30)  # 級数を2乗に修正

    # 入力を逐次処理
    while True:
        line = ''
        # 空行をスキップしつつM,Wを取得
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                return  # 入力終了
        M_W = line.strip().split()
        if len(M_W) < 2:
            continue
        M, W = map(int, M_W)
        if M == 0 and W == 0:
            break

        # 雄個体のB粒子のリストを取得
        while True:
            bm_line = sys.stdin.readline()
            if not bm_line:
                return
            bm_list = bm_line.strip().split()
            if len(bm_list) >= M:
                bm = list(map(int, bm_list))
                break
        # 雌個体のB粒子のリストを取得
        while True:
            bw_line = sys.stdin.readline()
            if not bw_line:
                return
            bw_list = bw_line.strip().split()
            if len(bw_list) >= W:
                bw = list(map(int, bw_list))
                break

        # dp[i][j]を定義: 雄i人目まで、雌j人目までの最大エネルギー
        # ただし、最大12人なので 全組み合わせマッチング問題としてbit DPを使う
        # 男性数M <=12なのでbitmaskで女の割り当てを管理し、配列もDPで最大化を計算する

        # 雄の人数M, 雌の人数W
        # W<=12なので、女の割当て状況をビットマスクで管理
        # dp[i][bit]: i番目の雄まで考慮した時にbitで示される雌を割り当てた状態の最大エネルギー

        from collections import defaultdict

        dp = [defaultdict(lambda: -1) for _ in range(M + 1)]
        dp[0][0] = 0  # 何も割り当てない状態は0

        for i in range(M):
            for mask, val in dp[i].items():
                # 今の雄( i番目 )をどの雌と組み合わせるか探索
                for j in range(W):
                    if (mask & (1 << j)) == 0:  # j番目の雌がまだ割り当てられていない
                        # エネルギー計算
                        diff = abs(bm[i] - bw[j])
                        energy = diff * (diff - 30) * (diff - 30)  # (|bm-bw| × (|bm-bw|-30)^2)

                        new_mask = mask | (1 << j)
                        new_val = val + energy
                        if dp[i + 1][new_mask] < new_val:
                            dp[i + 1][new_mask] = new_val
                # この雄を割り当てない場合(　合体しない＝エネルギー発生なし)も可能
                # 問題文で「合体した微生物のさらなる合体はない」のみだが、割当なしはOK
                # → 割当なしはdp[i+1][mask]更新
                if dp[i + 1][mask] < val:
                    dp[i + 1][mask] = val

        # 最大値探索
        max_energy = max(dp[M].values())
        print(max_energy)

if __name__ == "__main__":
    max_electric_energy()