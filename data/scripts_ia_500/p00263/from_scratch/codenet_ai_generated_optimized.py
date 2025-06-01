import sys

input = sys.stdin.readline
Q = int(input())
for _ in range(Q):
    s = input().strip()
    n = int(s, 16)
    sign = -1 if (n >> 31) & 1 else 1
    integer = (n >> 7) & ((1 << 24) -1)
    fraction = n & ((1 << 7) -1)
    # fraction = sum of b_i * (0.5)^i for i=1 to 7
    frac_val = fraction / 128
    val = sign * (integer + frac_val)
    # Format output according to instructions:
    # if fractional part is 0, print .0
    # else, remove trailing zeros in fractional part
    if val == 0.0:
        # check sign of zero
        # Using copysign to detect sign of zero
        import math
        if math.copysign(1.0, val) < 0:
            print("-0.0")
        else:
            print("0.0")
        continue
    s_val = str(val)
    if '.' in s_val:
        int_part, frac_part = s_val.split('.')
        frac_part = frac_part.rstrip('0')
        if frac_part == '':
            frac_part = '0'
        print(f"{int_part}.{frac_part}")
    else:
        print(s_val + ".0")