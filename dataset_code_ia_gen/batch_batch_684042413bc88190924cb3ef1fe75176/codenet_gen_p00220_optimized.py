def float_to_bin(num):
    if num < 0:
        return None
    integer_part = int(num)
    fractional_part = num - integer_part
    int_bin = bin(integer_part)[2:]
    if len(int_bin) > 8:
        return None
    int_bin = int_bin.zfill(8)
    frac_bin = []
    frac = fractional_part
    for _ in range(4):
        frac *= 2
        bit = int(frac)
        frac_bin.append(str(bit))
        frac -= bit
    if frac != 0:
        return None
    return int_bin + '.' + ''.join(frac_bin)

import sys
for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    try:
        n = float(line)
    except:
        continue
    if n < 0:
        break
    res = float_to_bin(n)
    print(res if res is not None else "NA")