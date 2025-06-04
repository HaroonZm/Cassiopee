from math import gcd

s = input()

if '(' not in s:
    # 有限小数の処理
    if '.' not in s:
        # 整数のみ
        num = int(s)
        den = 1
    else:
        integer_part, decimal_part = s.split('.')
        numerator = int(integer_part + decimal_part)
        denominator = 10 ** len(decimal_part)
        g = gcd(numerator, denominator)
        numerator //= g
        denominator //= g
        num = numerator
        den = denominator
else:
    # 循環小数の処理
    integer_part, rest = s.split('.')
    non_repeating_part = ''
    repeating_part = ''
    idx_start = rest.find('(')
    non_repeating_part = rest[:idx_start]
    repeating_part = rest[idx_start+1:-1]

    # 公式による分数化
    a = int(integer_part) if integer_part else 0
    b = non_repeating_part
    c = repeating_part

    if b == '':
        b = '0'
    n = len(b)
    k = len(c)

    # 分子 = a*(10^(n+k) - 10^n) + b*(10^k -1) + c
    numerator = a * (10**(n+k) - 10**n) + int(b)*(10**k -1) + int(c)
    denominator = (10**(n+k) - 10**n)

    g = gcd(numerator, denominator)
    num = numerator // g
    den = denominator // g

print(str(num) + '/' + str(den))