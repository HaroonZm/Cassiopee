import sys

MP = 999983
# 2007年11月の既知の素数リストを用意
# 1000000以下の素数と末端の2つの素数999979, 999983のみ
# ここでは単純化のため1000000以下の素数は知られていないが、問題文で最大素数は999983とされている。
# よって素数判定は999979と999983を含めた判定とする。

# ただし問題文に以下の記述があるため、
# 「我々は1000003が素数であることを知っているが、この国では知られていません。
# そのため999963以上1000003以下では999979と999983だけが素数」
# なので、100万以下の素数は知られているはず(≒999983までの素数)
# 数が多すぎて全て覚えずに済むように素数判定はエラトステネス篩などの辞書を作るのはダメ
# → 999983以下の素数一覧は大量なので実装困難。
# → 簡単のため、問題文が欲しいのは素数カウントのみなので、素数判定関数を用意し、線形で処理。
# → MP=999983は最大なので、mを加減して範囲検索する場合は素数判定だけすればよい。

# 素数判定はシンプルにsqrtでやる。

import math

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    limit = int(math.sqrt(x)) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            return False
    # 2007年11月時点で知られてない素数は999983以上なら999979と999983のみ
    # なので1000000以上はすべて素数ではない扱いにする（問題の条件）
    if x > MP:
        # 1000000超えは素数扱いされない
        return False
    return True

def count_primes_in_range(a, b):
    count = 0
    start = max(a, 0)
    end = min(b, MP)
    for num in range(start, end + 1):
        # この国で知られている素数は999983以下で判定可能
        # ただし999979と999983は特別扱い（上で真に判定済み）
        if is_prime(num):
            count += 1
    return count

def main():
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n_str = input_lines[idx].strip()
        idx += 1
        if n_str == '0':
            break
        n = int(n_str)
        # pごとの賞金をまとめる辞書
        prize_sum = dict()
        for _ in range(n):
            p_str, m_str = input_lines[idx].split()
            idx += 1
            p = int(p_str)
            m = int(m_str)
            lower = p - m
            upper = p + m
            x = count_primes_in_range(lower, upper)  # 個数X
            # 当選者への支払いはXプライムだが、X=0は0プライム
            if p in prize_sum:
                prize_sum[p] += x
            else:
                prize_sum[p] = x
        # 宝くじ振興公社が王様に請求する額は
        # (X-1)プライムを当たりくじ1本ごとに合計したもの（X≥1の分のみ）
        # X=0なら請求額0
        total_cost = 0
        for p in prize_sum:
            total_cost += max(prize_sum[p] - 1, 0)
        print(total_cost)

if __name__ == '__main__':
    main()