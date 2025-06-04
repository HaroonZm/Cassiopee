# 入力された文字列は、整数部、小数部非循環部分、循環部分から成る可能性がある
# 例えば、"5.2(143)"なら
#   整数部 = 5
#   非循環小数部 = 2
#   循環小数部 = 143
#
# 実数を分数に変換する方法：
# 実数 = 整数部 + 非循環小数部 / (10^(非循環小数の桁数)) + 循環小数部/(10^(非循環の桁数)*(10^(循環の桁数)-1))
#
# 例："0.(3)" => 0 + 0 + 3/9 = 1/3
#       "5.2(143)" => 5 + 2/10 + 143/(10*999) = (計算後に既約分数化)
#
# すべてを分母の公倍数にして、分子を一つの整数にまとめてから最大公約数で約分する。
#
# 循環がない場合は単純に整数部 + 小数分数として扱えば良い。

def gcd(a, b):
    # 最大公約数をユークリッドの互除法で求める
    while b:
        a, b = b, a % b
    return a

def convert_to_fraction(s):
    # 文字列の解析
    # "("があるかで循環有無を判定
    if "(" in s:
        # 循環小数ありのケース
        # ex: 5.2(143) -> 整数部=5 小数非循環=2 循環=143
        # 形式は必ず  "整数部.非循環(循環)"で与えられるので、
        # "."位置と "("")位置を使って切り出す
        dot_idx = s.index(".")
        paren_start = s.index("(")
        paren_end = s.index(")")

        integer_part = int(s[:dot_idx])
        non_repeat_decimal = s[dot_idx+1:paren_start]  # 非循環小数部の文字列
        repeat_decimal = s[paren_start+1:paren_end]   # 循環小数部の文字列
        
        # 長さを取る
        len_non_repeat = len(non_repeat_decimal)
        len_repeat = len(repeat_decimal)
        
        # 分母は
        # 10^len_non_repeat * (10^len_repeat - 1)
        denom = (10**len_non_repeat) * (10**len_repeat - 1)
        
        # 分子は、全ての小数部分を整数として扱うために
        # 全小数を繋げたもの - 非循環部分だけの整数を差し引く
        # 例："0.2(143)" -> 全ての小数部分は "2143" -> int("2143")
        # 非循環部分は "2" -> int("2")
        # integer_partは後で足す
        
        full_decimal_str = non_repeat_decimal + repeat_decimal
        num_decimal_full = int(full_decimal_str) if full_decimal_str else 0
        num_decimal_non_repeat = int(non_repeat_decimal) if non_repeat_decimal else 0
        
        numerator_decimal = num_decimal_full - num_decimal_non_repeat
        
        # 全分子は、整数部分を分母分だけ拡大して加算
        numerator = integer_part * denom + numerator_decimal
        
    else:
        # 循環小数なしケース
        # ex: "1.0", "0.0739"
        if "." in s:
            integer_part_str, decimal_part_str = s.split(".")
            integer_part = int(integer_part_str)
            decimal_part = decimal_part_str
            len_decimal = len(decimal_part)
            denom = 10 ** len_decimal
            numerator = integer_part * denom + int(decimal_part)
        else:
            # 少数点すらない (問題の条件ではないが念のため)
            numerator = int(s)
            denom = 1
    
    # 約分
    g = gcd(numerator, denom)
    numerator //= g
    denom //= g
    
    return f"{numerator}/{denom}"

# 入力受け取り
s = input().strip()
print(convert_to_fraction(s))