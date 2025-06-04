import sys
import bisect

# 最大の素数 MP。問題文により 999983（1000000以下の最大素数）
MP = 999983

# 問題文により 1 は素数じゃない
# 2007年11月時点で知られている素数は MP 以下のすべて
# ここでは素数リストを作る必要がある。
# 上限は1000000まで（MP=999983)
# エラトステネスの篩を用いて素数リストを作成。

def sieve(max_n):
    """エラトステネスの篩でmax_nまでの素数リストを返す"""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n+1, i):
                is_prime[j] = False
    primes = [i for i, val in enumerate(is_prime) if val]
    return primes

primes = sieve(1000000)

# primesは昇順の素数リスト
# 賞金Xは、p - m 以上 p + m 以下の素数の個数
# この区間の素数の個数は primes における区間のインデックス差で求められる

def count_primes_in_range(left, right):
    """left <= 素数 <= right の個数を返す"""
    # left未満の値より大きい最初の素数の位置を求める
    # right以下の最後の素数の位置を求める
    # bisect_left(primes, left)は左端位置
    # bisect_right(primes, right)は右端の次の位置
    left_pos = bisect.bisect_left(primes, left)
    right_pos = bisect.bisect_right(primes, right)
    return right_pos - left_pos

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        n = line.strip()
        if n == '0':
            break
        n = int(n)
        # 各当たりくじ p,m 読取
        lottery_map = dict()  # p -> 合計賞金Xの合計
        for _ in range(n):
            line = input()
            if not line:
                break
            p_str, m_str = line.strip().split()
            p = int(p_str)
            m = int(m_str)
            left = p - m
            right = p + m
            if left < 0:
                left = 0
            if right > MP:
                right = MP
            X = count_primes_in_range(left, right)
            # X=0でも記録しておく。後でnを数えるのに必要。
            # 複数当たりくじが同じpなら合計する
            lottery_map[p] = lottery_map.get(p, 0) + X

        # 当たりくじ本数 n = 当たり番号の総数
        # 1サブプライム = 1/101 プライム
        # 1プライム = 101サブプライム
        # 当たりくじ一本あたり公社負担1プライム
        # 内廷費支払額を求める
        #
        # 賞金Xプライムのうち1プライムは宝くじ売り上げ（公社負担）
        # X-1が王様の内廷費から支出される（X>=1の場合）
        # X=0なら売上から1プライムが内廷費に繰り入れられる
        # 当たりくじ本数 n は宝くじ販売本数/101以下にすることで赤字はない。
        #
        # 求めるのは 王様に請求する賞金の合計 = 内廷費支払額の合計
        # ＝ sum( (X-1) if X>=1 else 0 ) + sum(1 for X=0)
        #
        # Xが当たりくじごとに合計されているので計算できる。

        inner_expense = 0
        for X in lottery_map.values():
            if X >= 1:
                inner_expense += (X - 1)
            else:
                # X=0の賞金は当選者には出ないが、売上から1プライムが内廷費繰入として入る
                # 抽選結果から算出される賞金は0だけど、"X=0ならば宝くじの売上から1プライムが内廷費に繰入れ"
                # 当たりくじの本数 = len(lottery_map) = n_当たりくじ番号数なので足すべきか？
                # この中のX=0の分のみ1プライム繰入
                inner_expense += 1

        # 内廷費の請求額は負にならないとあるので負チェック不要
        print(inner_expense)

if __name__ == '__main__':
    main()