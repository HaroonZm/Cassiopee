from math import gcd

s = input()

if '(' not in s:
    # 有限小数
    if '.' in s:
        int_part, dec_part = s.split('.')
    else:
        int_part, dec_part = s, ''
    numerator = int(int_part + dec_part)
    denominator = 10 ** len(dec_part)
else:
    # 循環小数
    int_part, rest = s.split('.')
    non_recur, recur = rest.split('(')
    recur = recur[:-1]
    a = int(int_part) if int_part else 0
    # 整数部 + 非循環部 + 循環部の結合値
    full_num = int(int_part + non_recur + recur)
    # 整数部 + 非循環部の結合値
    non_recur_num = int(int_part + non_recur) if int_part+non_recur else 0
    len_non_recur = len(non_recur)
    len_recur = len(recur)
    numerator = full_num - non_recur_num
    denominator = 10 ** (len_non_recur + len_recur) - 10 ** len_non_recur

g = gcd(numerator, denominator)
print(f"{numerator//g}/{denominator//g}")