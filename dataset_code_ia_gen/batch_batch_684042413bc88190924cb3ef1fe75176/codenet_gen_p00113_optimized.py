import sys

for line in sys.stdin:
    if not line.strip():
        continue
    p, q = map(int, line.split())
    p = p % q
    decimal_digits = []
    remainder_pos = {}
    idx = 0
    while True:
        if p == 0:
            # 有限小数
            print(''.join(decimal_digits))
            break
        if p in remainder_pos:
            # 循環小数
            start = remainder_pos[p]
            non_repeating = ''.join(decimal_digits[:start])
            repeating = ''.join(decimal_digits[start:])
            print(non_repeating + repeating)
            print(' ' * len(non_repeating) + '^' * len(repeating))
            break
        remainder_pos[p] = idx
        p *= 10
        decimal_digits.append(str(p // q))
        p %= q
        idx += 1