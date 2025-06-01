# このプログラムは、電子蝿の戻り回数を計算する問題を解きます。
# 電子蝿の座標遷移は次の式で与えられます：
# x' = (a1 * x) mod m1
# y' = (a2 * y) mod m2
# z' = (a3 * z) mod m3
# 初期点は (1, 1, 1) であり、この点に再び戻るまでの最小移動回数（正の整数）を求めます。
# 条件として、それぞれ (a1,m1), (a2,m2), (a3,m3) が互いに素であることが保証されています。

# アプローチ：
# 1. 各座標軸について:
#    a. x軸を例にすると、 xの遷移は x_n = (a1^n) mod m1 となる。
#    b. よって、あるnで (a1^n) ≡ 1 (mod m1) となる最小nを求めれば良い。
# 2. 各軸のこうしたnをそれぞれ計算し、最終的な周期は3つの周期の最小公倍数となる。
# 3. 最小公倍数を計算し、それを出力する。
# 
# ポイント：
# - モジュラ指数演算は pow(base, exp, mod) で高速に計算できる。
# - 最小周期（オーダー）を求めるため、mは最大32767程度だが、効率化のためオーダーはmのオイラー関数に関係し、mの約数を調べて試行する方法をとる。
# - 公約数が1なのでオイラー関数は計算しやすい。

from math import gcd

def euler_phi(n):
    # nのオイラーのトーテント関数を計算
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1 if p==2 else 2
    if n > 1:
        result -= result // n
    return result

def order(a, m):
    # a と m は互いに素であることが前提
    # オーダーを求める: a^k ≡ 1 (mod m)となる最小の正整数k
    phi = euler_phi(m)  # オイラー関数
    # phiの約数を調べて、a^d mod m == 1 となる最小のdを求める
    # 約数列挙
    divisors = []
    i = 1
    while i*i <= phi:
        if phi % i == 0:
            divisors.append(i)
            if i != phi // i:
                divisors.append(phi // i)
        i += 1
    divisors.sort()
    for d in divisors:
        if pow(a, d, m) == 1:
            return d
    return phi  # 何らかの理由で見つからなければphiを返すが、通常はここに来ない。

def lcm(a, b):
    return a // gcd(a, b) * b

def main():
    while True:
        line = input().strip()
        if not line:
            continue
        a1, m1, a2, m2, a3, m3 = map(int, line.split())
        if a1 == 0 and m1 == 0 and a2 == 0 and m2 == 0 and a3 == 0 and m3 == 0:
            break
        
        # 各軸についてオーダーを求める
        order_x = order(a1, m1)
        order_y = order(a2, m2)
        order_z = order(a3, m3)
        
        # 最小移動回数は3つの周期の最小公倍数
        res = lcm(lcm(order_x, order_y), order_z)
        print(res)

if __name__ == "__main__":
    main()