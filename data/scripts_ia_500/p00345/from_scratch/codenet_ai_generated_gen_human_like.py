from math import gcd

def to_fraction(s):
    if '(' not in s:
        # 有限小数の場合
        if '.' in s:
            integer_part, decimal_part = s.split('.')
            numerator = int(integer_part + decimal_part)
            denominator = 10 ** len(decimal_part)
        else:
            numerator = int(s)
            denominator = 1
    else:
        # 循環小数の場合
        integer_part, rest = s.split('.')
        non_repeating = ''
        repeating = ''
        i = 0
        while rest[i] != '(':
            non_repeating += rest[i]
            i += 1
        i += 1  # '(' の次
        while rest[i] != ')':
            repeating += rest[i]
            i += 1

        n = len(non_repeating)
        r = len(repeating)

        I = int(integer_part)
        if non_repeating == '':
            non_repeating_val = 0
        else:
            non_repeating_val = int(non_repeating)
        repeating_val = int(repeating)

        numerator = (I * (10 ** (n + r)) +
                     non_repeating_val * (10 ** r) +
                     repeating_val -
                     (I * (10 ** n) + non_repeating_val))
        denominator = (10 ** (n + r) - 10 ** n)

    g = gcd(numerator, denominator)
    numerator //= g
    denominator //= g
    print(f"{numerator}/{denominator}")

s = input()
to_fraction(s)