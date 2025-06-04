import sys
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a // gcd(a, b) * b

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        nums = []
        denoms = []
        for _ in range(n):
            d, v = map(int, input().split())
            # 周回時間 = d/v
            # 全員の周回時間の最小公倍数を分数で扱うため分母と分子の形で管理
            # => 周回時間の通分用に求める
            gcddv = gcd(d, v)
            di = d // gcddv
            vi = v // gcddv
            nums.append(di)
            denoms.append(vi)

        # 全員の周回時間の最小公倍数 = LCM_分子 / GCD_分母 (分数の形)
        # まず分母の最大公約数
        g_denom = denoms[0]
        for v in denoms[1:]:
            g_denom = gcd(g_denom, v)

        # 次に分子の最小公倍数
        l_num = nums[0]
        for d_ in nums[1:]:
            l_num = lcm(l_num, d_)

        # 最小公倍数の時間を分数で表すと l_num / g_denom
        # 各生徒の周回数 = (最小公倍数の時間) / (自分の周回時間)
        # = (l_num / g_denom) / (nums[i] / denoms[i]) = (l_num / g_denom) * (denoms[i] / nums[i])
        # = (l_num * denoms[i]) / (g_denom * nums[i])
        # 整数になるはずなので整数除算で出力

        for i in range(n):
            val = (l_num * denoms[i]) // (g_denom * nums[i])
            print(val)

if __name__ == "__main__":
    main()