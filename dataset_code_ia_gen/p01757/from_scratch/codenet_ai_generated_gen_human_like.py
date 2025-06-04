import sys
sys.setrecursionlimit(10**7)

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    # チーム数
    size = 2 ** n

    # 入力の順位表を配列に展開
    rank = [0] * size
    for i in range(m):
        for j in range(a[i], a[i+1]):
            rank[j] = b[i]

    # dp関数をメモ化して無矛盾な結果にするための最小変更数を求める
    from functools import lru_cache

    # indexは区間の開始, lengthは区間の長さ
    @lru_cache(None)
    def dfs(index, length):
        if length == 1:
            # 1チームなら順位=2^n - 0 = 2^n - wins,
            # 勝った回数=0なので順位=2^n
            # 逆にn回勝てば順位=1
            # 個別のチームの順位は rank[index]
            # 現実の順位は2^n - wins なのでこの場所では順位は n - round_wins
            # length=1なので勝った回数=0 順位=2^n (最後尾)
            # ここでの勝った回数は0（順位は2^n）
            # 変更が必要かはrank[index]との差
            # 後でまとめて判定するからとりあえず変更数は0か1で考えず0にする
            # return {勝った回数: 変更最小数} とする
            return {0: 0}

        half = length // 2
        left = dfs(index, half)
        right = dfs(index + half, half)

        res = {}

        # 今回のラウンドで勝つチームは、左側か右側
        # 勝った回数がiのチームは今ラウンド0勝または1勝を加える
        # トーナメントラウンドがn - log2(length) +1 回目

        round_number = n - (length.bit_length() -1) +1

        # 左が勝つパターン
        for lw, lcost in left.items():
            for rw, rcost in right.items():
                # 左が勝って勝ち数+1
                win = lw + 1
                if win > n:
                    continue
                # 右は負けて勝ち数そのまま
                # 勝ち数別にコストが求まったら後で区間ごとに領域が決まるのでここでは足すだけ
                total_cost = lcost + rcost
                # この区間のチームは最終的にrankの区間[index:index+length]の順位にならなければいけない
                # 順位 = 2^n - winning_times
                # この範囲の順位は区間の中で同じ値なので外でチェック
                # ここでは可能な勝ち数と最小コストを記録
                prev = res.get(win, float('inf'))
                if total_cost < prev:
                    res[win] = total_cost

        # 右が勝つパターン
        for lw, lcost in left.items():
            for rw, rcost in right.items():
                # 右が勝って勝ち数+1
                win = rw +1
                if win > n:
                    continue
                total_cost = lcost + rcost
                prev = res.get(win, float('inf'))
                if total_cost < prev:
                    res[win] = total_cost

        # 現在の区間の順位(配列内は全部同じ)
        cur_rank = rank[index]
        # 正しい順位は 2^n - 勝った回数
        # i勝ちの勝った回数iに対し
        to_delete = float('inf')
        for w, cost in res.items():
            expected_rank = size - w
            if expected_rank == cur_rank:
                # 区間内の順位変更回数はcost + 各チームが変わっている数
                # 区間内のチームの順位は同じなので順位と合わない部分は全部変更が必要
                # 順位があっているのでcostだけでよい
                to_delete = min(to_delete, cost)
            else:
                # 順位が違う場合は
                # 全数変更分 length を加える必要あり
                # 変更されるのは区間内のすべてのチームなのでコストにlengthを足す
                to_delete = min(to_delete, cost + length)
        # 指定勝ち数であってない場合も上記で補正済みなので、ここは res を to_delete だけにしておく
        res = {w: to_delete for w in res.keys()}
        return res

    ans = min(dfs(0, size).values())
    print(ans)

if __name__ == '__main__':
    main()