# 解説：
# 問題はIDの各桁で、いくつかの桁が'*'で不明な部分がある。
# '*'には与えられた候補の数字が入るとき、IDが正しいかどうか判定し、
# 正しいIDとなる組み合わせの数を求めること。

# チェックルール：
# - 右端を1番目として、偶数番目の桁は2倍する
# - 16進計算で、2倍した数が10以上なら、桁を分解して足す（例えば14なら1+4=5）
# - 全桁の数字の合計が10で割り切れれば正しい

# 入力制約により、
# nは最大10万桁
# '*'は最大7個なので、組み合わせは最大10^7通りまで探索可
# しかし10^7も大きいのでDPで剰余を巧妙に計算して高速に処理する

# アプローチ：
# - 右端を1番目として各桁に対し、2倍チェック等の調整値を前処理で求めておく
# - 既知の桁は合計に加算
# - '*'の位置ごとに各候補数字を代入した場合の効果（合計への寄与）を考える
# - DPで各'*'の処理を連結し、最終的に合計が10の倍数になる組み合わせ数を求める

import sys
import threading

def main():
    n = int(sys.stdin.readline())
    ID = sys.stdin.readline().strip()
    m = int(sys.stdin.readline())
    candidates = list(map(int, sys.stdin.readline().split()))
    
    # 右端を1番目とするindex付け (1-based)
    # i番目の桁の補正値を計算
    # i=1が右端からなのでIDの末尾がi=1
    # 右端がi=1ならIDのインデックスは n - i
    # 1-basedとして扱うため便宜的にi=1~nで繰り返す
    # 偶数番目の桁は２倍し、10以上なら桁和をとる
    def digit_contribution(d, pos_from_right):
        if pos_from_right % 2 == 0:  # 偶数番目
            val = d * 2
            if val >= 10:
                val = (val // 10) + (val % 10)
            return val
        else:
            return d

    # '*'の位置を収集し、その位置ごとに補正係数を求める
    star_positions = []
    # 既に決まっている桁の合計
    fixed_sum = 0
    
    # n桁の位置 i=1:左端, i=n:右端とすると扱いづらいので右端1と揃えるためiは1～n
    # IDのインデックスは0～n-1
    # 右端がpos=1ならIDのインデックスは n - pos
    for pos_from_right in range(1, n+1):
        c = ID[n - pos_from_right]
        if c == '*':
            star_positions.append(pos_from_right)
        else:
            fixed_sum += digit_contribution(int(c), pos_from_right)
    
    # '*'の個数
    star_num = len(star_positions)
    
    # DPテーブル: dp[i][r] = i個の'*'まで決めて合計を10で割った余りrの組み合わせ数
    # 余りは0~9の10通り
    # 初期は0個で余りが fixed_sum % 10 となるものが1
    mod = 10
    dp = [0]*mod
    dp[fixed_sum % mod] = 1
    
    # '*'それぞれに候補の数字を入れた時の寄与を計算しDP更新
    for pos in star_positions:
        new_dp = [0]*mod
        # その桁の寄与の計算用関数はdigit_contribution
        for r in range(mod):
            if dp[r] == 0:
                continue
            cnt = dp[r]
            for d in candidates:
                val = digit_contribution(d, pos)
                nr = (r + val) % mod
                new_dp[nr] += cnt
        dp = new_dp
    
    # 最終的に余りが0なら正しいID
    print(dp[0])

threading.Thread(target=main,).start()