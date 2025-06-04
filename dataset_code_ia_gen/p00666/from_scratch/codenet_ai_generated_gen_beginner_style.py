import sys
sys.setrecursionlimit(10**7)

MOD = 100000007

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        p = [0]*n
        id_ = [0]*n
        w = [0]*n
        for i in range(n):
            line = input().split()
            p[i] = float(line[0])
            id_[i] = int(line[1])
            w[i] = float(line[2])

        full = (1<<n)-1
        # dp_time[s] =期待時間残りロボットがsに含まれる状態から全滅まで
        # dp_count[s] =組み合わせ数
        dp_time = [-1.0]*(1<<n)
        dp_count = [0]*(1<<n)

        def dfs(s):
            if s == 0:
                dp_time[0] = 0.0
                dp_count[0] = 1
                return (0.0, 1)
            if dp_time[s] >= 0:
                return (dp_time[s], dp_count[s])

            min_time = 1e100
            ways = 0

            alive = []
            for i in range(n):
                if (s>>i)&1:
                    alive.append(i)

            # R博士のロボットは既に奪った武器チップで敗北確率変わる
            # 奪った武器は、sの範囲の外のロボットの武器チップ
            # 相手がその武器を持ってるかチェック->奪ってるかで判別
            for now in alive:
                # nowを攻撃対象にする
                # 負け確率と期待時間計算
                # 敵は武器チップを奪っている武器チップはsにいない（撃破）
                # nowの弱点はid_[now]
                if ((s>>(id_[now]))&1) == 0:
                    # 弱点武器を敵は持ってる
                    lose_prob = w[now]
                else:
                    # 持ってない
                    lose_prob = p[now]

                if lose_prob == 1.0:
                    # 今のロボットが必ず負けて破壊される
                    next_s = s & ~(1<<now)
                    next_time, next_ways = dfs(next_s)
                    cur_time = 1 + next_time
                    if cur_time < min_time-1e-12:
                        min_time = cur_time
                        ways = next_ways
                    elif abs(cur_time - min_time) < 1e-12:
                        ways = (ways + next_ways)%MOD
                    continue

                # 確率
                # ロボット今のが負けなら状態はnext_s
                next_s = s & ~(1<<now)
                next_time, next_ways = dfs(next_s)

                # 敵負けなら状態は変わらずs
                # 独立で期待値計算すると 1 + lose_prob * next_time + (1-lose_prob)*dp_time[s]
                # → dp_time[s] = 1 + lose_prob * next_time + (1-lose_prob) * dp_time[s]
                # → dp_time[s] - (1-lose_prob)*dp_time[s] = 1 + lose_prob * next_time
                # → dp_time[s]*lose_prob = 1 + lose_prob * next_time
                # → dp_time[s] = (1 + lose_prob * next_time)/lose_prob
                # 今回は複数のnowを試すので加味
                # 以上は1個のnowを反復した場合の期待時間
                # 戦略はR博士が一番早い戦術選ぶ⇒最小期待値を選ぶので、全部試して最小を取る

                cur_time = (1 + lose_prob * next_time)/lose_prob

                if cur_time < min_time-1e-12:
                    min_time = cur_time
                    # 残りは次状態がnext_sなら方式数はnext_ways
                    # ここも注意、複数のnowで最小期待値同時に達成するなら加算
                    ways = next_ways
                elif abs(cur_time - min_time) < 1e-12:
                    ways = (ways + next_ways)%MOD

            dp_time[s] = min_time
            dp_count[s] = ways % MOD
            return (dp_time[s], dp_count[s])

        ans_time, ans_count = dfs(full)
        print("%.11f %d" % (ans_time, ans_count % MOD))

if __name__ == "__main__":
    main()