from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

while True:
    a1, m1, a2, m2, a3, m3 = map(int, input().split())
    if a1 == 0 and m1 == 0 and a2 == 0 and m2 == 0 and a3 == 0 and m3 == 0:
        break
    # Since a_i and m_i are coprime, the cycle length in each coordinate is m_i
    # The total cycle length is LCM of m1, m2, m3
    ans = lcm(lcm(m1, m2), m3)
    print(ans)