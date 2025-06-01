# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**7)

def main():
    MOD = 10000
    
    N, K = map(int, input().split())
    fixed = [0] * (N+1)  # 固定されている日ごとのパスタ（0:未定, 1:トマト, 2:クリーム, 3:バジル）
    for _ in range(K):
        day, pasta = map(int, input().split())
        fixed[day] = pasta
    
    # dp配列の定義:
    # dp[i][pasta][count] := 
    # i日目まで決めたときの、i日目がpasta（1..3）、連続してpastaがcount日続いている場合の総数
    # count は 1 or 2（3日連続は不可なのでそれ以上は考えない）
    dp = [[[0]*3 for _ in range(4)] for _ in range(N+1)]
    # 初期化
    # 0日目、まだ何も決まっていない状態として、特別な状態を置く必要はないので
    # 1日目の初期値をセットする
    
    # 1日目のパスタ決定
    if fixed[1] != 0:
        # 1日目が既に決まっている場合
        dp[1][fixed[1]][0] = 1  # count=0 は使わないので count=1はindex0で扱う
    else:
        # 1日目が自由に選べる場合
        for p in range(1,4):
            dp[1][p][0] = 1
    
    # dpでcountを0ベースで管理するために、
    # count=1 → dp index 0
    # count=2 → dp index 1
    
    for i in range(2, N+1):
        for p in range(1,4):  # 今日のパスタ種類
            # もし日iのパスタが決まっていれば、それ以外のパスタは0でスキップ
            if fixed[i] !=0 and fixed[i] != p:
                continue
            for q in range(1,4):  # 前日のパスタ種類
                for count_index in range(2):  # 前日の連続日数(0:1日目、1:2日目)
                    # 連続している日数は count_index+1 日連続していると考える
                    if p == q:
                        # 同じパスタが続く場合
                        # 3日目以降は不可なので、countは最大2まで
                        if count_index == 1:
                            # すでに2日連続なので3日目はNG
                            continue
                        dp[i][p][count_index+1] += dp[i-1][q][count_index]
                        dp[i][p][count_index+1] %= MOD
                    else:
                        # 違うパスタなら連続は1日目にリセット
                        dp[i][p][0] += dp[i-1][q][count_index]
                        dp[i][p][0] %= MOD
    
    # 最終日の答えはdp[N][p][count]のすべてのp,countの和
    ans = 0
    for p in range(1,4):
        for count_index in range(2):
            ans += dp[N][p][count_index]
    print(ans % MOD)

if __name__ == "__main__":
    main()