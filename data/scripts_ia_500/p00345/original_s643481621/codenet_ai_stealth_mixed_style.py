from math import gcd

def fraction_from_decimal(s):
    if "(" in s:
        x, y = s.split(".")
        start = y.index("(")
        end = y.index(")")
        non_repeating = y[:start]
        repeating = y[start+1:end]
        base_num = int(x + non_repeating) if non_repeating else int(x)
        len_non_rep = len(non_repeating)
        len_rep = len(repeating)
        numerator = base_num * (10**len_rep - 1) + int(repeating)
        denominator = (10**len_non_rep) * (10**len_rep - 1)
        g = gcd(numerator, denominator)
        return numerator // g, denominator // g
    else:
        parts = s.split(".")
        whole = int(parts[0])
        frac = parts[1]
        numerator = int(parts[0] + frac)
        denominator = 10**len(frac)
        g = gcd(numerator, denominator)
        return numerator // g, denominator // g

input_str = input()
result = fraction_from_decimal(input_str)
print(f"{result[0]}/{result[1]}")