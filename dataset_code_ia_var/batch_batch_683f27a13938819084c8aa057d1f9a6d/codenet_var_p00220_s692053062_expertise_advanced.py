import sys

def float_to_bin_fixed(f: float) -> str:
    if not (0.0 <= f < 256.0):
        return 'NA'
    frac, whole = math.modf(f * 16)
    int_part = int(whole)
    if frac:
        return 'NA'
    bin_repr = f"{int_part:012b}"
    return f"{bin_repr[:-4]}.{bin_repr[-4:]}"

import math
def main():
    for line in sys.stdin:
        try:
            f = float(line)
        except ValueError:
            continue
        if f < 0.0:
            break
        print(float_to_bin_fixed(f))

if __name__ == "__main__":
    main()