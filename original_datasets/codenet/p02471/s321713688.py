def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    a, b = map(int, input().split())
    if a == b or a % b == 0:
        print(0, 1)
    elif b % a == 0:
        print(1, 0)
    else:
        g = gcd(a, b)
        a //= g
        b //= g
        coe = [[1, 0], [0, 1]]
        while b != 1:
            quo = a // b
            coe_d1 = coe[1]
            coe_d2 = [coe[0][0] - coe[1][0] * quo, coe[0][1] - coe[1][1] * quo]
            coe = [coe_d1, coe_d2]
            a, b = b, a % b
        print(*coe[1])

solve()