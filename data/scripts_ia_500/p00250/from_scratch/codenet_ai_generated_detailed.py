# この問題では、連続した範囲のお盆を選び、その範囲内にあるスコーンの合計をmで割った余りを最大化したい。
# つまり、数列のある区間の和のmでの剰余の最大値を求める問題となる。

# アプローチ：
# 1. まず、スコーンの数列の部分和を計算する。
#    prefix[i] = K_1 + K_2 + ... + K_i
#    便宜上prefix[0] = 0 とする。
#
# 2. 区間[i, j]の和は prefix[j] - prefix[i-1] で求まる。
#    余りは (prefix[j] - prefix[i-1]) % m となる。
#
# 3. この式を変形すると、
#    (prefix[j] - prefix[i-1]) % m = (prefix[j] % m - prefix[i-1] % m + m) % m
#
# 4. したがって、prefixの余り列を考え、i < j について
#    (prefix[j] - prefix[i]) % m を最大化する問題に帰着する。
#
# 5. 余り配列prefix_modを昇順に走査しながら、
#    辞書順の昇順でprefix_modを考えるので、prefix_mod[j] - prefix_mod[i]の最大値を求めるのは難しいが、
#    順番はprefix_modの配列の元々の順序に従うため、i < jかつprefix_mod[i] >= prefix_mod[j]の場合に最大の余りが得られる。
#
# 6. よって、
#    走査時にこれまで見たprefix_modの要素を順に管理し、
#    prefix_mod[j]より大きい値を二分探索などで見つけて、余りを計算し、
#    最大値を更新する。
#
#    しかし、mは最大10万なので、簡単にO(n log n)で解ける。
#
# 実装方針：
# - prefix_modを計算しつつ、
# - 過去のprefix_modで自分より大きい値を見つけたら、(prefix_mod[j] - その値 + m) % m が余りの候補になる。
# - または、prefix_modの中で自分より大きい最小の値を見つけ、その差で最大余りを計算。
# - さらに、prefix_mod自身もmax(prefix_mod[j], 現在の最大値)を更新することを忘れない。

# 以下はコード実装例。

import sys
import bisect

def max_remainder(n, m, K):
    # prefix_mod: prefix和のmod mを格納
    prefix_mod = [0]
    s = 0
    for x in K:
        s += x
        prefix_mod.append(s % m)

    result = 0
    # ソート済みのprefix_modの中で自身より大きい最小の値を探すためのリストを管理
    sorted_list = []
    for val in prefix_mod:
        # bisect_rightでvalより大きい最小の値のindexを探す
        # valより大きい値があれば、その値をpとする
        # 現在の余り候補は (val - p + m) % m
        idx = bisect.bisect_right(sorted_list, val)
        if idx < len(sorted_list):
            # sorted_list[idx]はvalより大きい最小の値
            candidate = (val - sorted_list[idx] + m) % m
            if candidate > result:
                result = candidate
        if val > result:
            result = val
        bisect.insort(sorted_list, val)
    return result

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    pos = 0
    while True:
        if pos >= len(input_lines):
            break
        line = input_lines[pos].strip()
        pos += 1
        if line == '0 0':
            break
        n, m = map(int, line.split())
        K = list(map(int, input_lines[pos].strip().split()))
        pos += 1
        print(max_remainder(n, m, K))

if __name__ == '__main__':
    main()