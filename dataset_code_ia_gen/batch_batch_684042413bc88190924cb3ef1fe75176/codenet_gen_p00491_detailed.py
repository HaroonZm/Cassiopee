# 解法のポイント
# 1. 動的計画法 (DP) を用いる。
# 2. 各日の料理は3種類（1: トマトソース, 2: クリームソース, 3: バジルソース）のいずれかを選択。
# 3. 同じパスタが3日以上連続しないように制約を入れる。
# 4. N日で、決まった日のメニュー情報が K 個 与えられる（固定メニュー）。
# 5. DP の状態としては、(日付, 前日のパスタ, 連続して食べた回数) を持ち、次の日の候補を計算していく。
# 6. 最後に該当する全ての状態の和が答えになる。
# 7. 答えは10000で割った余りを出力する。

import sys
sys.setrecursionlimit(10**7)

def main():
    MOD = 10000

    N, K = map(int, input().split())
    fixed = [0]*(N+1)  # 1-indexedで日付ごとに固定のパスタ情報(0=なし,1=トマト,2=クリーム,3=バジル)
    for _ in range(K):
        Ai, Bi = map(int, input().split())
        fixed[Ai] = Bi

    # dp[day][last_pasta][count] = その日の最後のパスタがlast_pastaで連続回数がcountの場合の予定数
    # day: 1からNまで
    # last_pasta: 1,2,3
    # count: 1または2 (3以上はNG)
    dp = [[[0]*3 for _ in range(4)] for _ in range(N+1)]

    # 初日の初期化
    # 初日はcount=1で開始
    if fixed[1] != 0:
        dp[1][fixed[1]][1] = 1
    else:
        for pasta in range(1,4):
            dp[1][pasta][1] = 1

    for day in range(2, N+1):
        for last_pasta in range(1,4):
            for count in range(1,3):  # countは1か2のみ
                if dp[day-1][last_pasta][count] == 0:
                    continue
                # 次の日に選べるパスタ
                for next_pasta in range(1,4):
                    # 固定されたパスタがあれば、そのパスタのみ選択可能
                    if fixed[day] != 0 and fixed[day] != next_pasta:
                        continue
                    # 同じパスタが3日連続にならないように
                    if next_pasta == last_pasta:
                        if count == 2:
                            continue  # 連続3日目はNG
                        dp[day][next_pasta][count+1] = (dp[day][next_pasta][count+1] + dp[day-1][last_pasta][count]) % MOD
                    else:
                        # 新しいパスタを選んだので連続回数は1にリセット
                        dp[day][next_pasta][1] = (dp[day][next_pasta][1] + dp[day-1][last_pasta][count]) % MOD

    ans = 0
    for last_pasta in range(1,4):
        for count in range(1,3):
            ans = (ans + dp[N][last_pasta][count]) % MOD

    print(ans)

if __name__ == "__main__":
    main()