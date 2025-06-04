from functools import reduce
import sys

pos = [0, 1, 2, 0, -1, 2, 0, 1, 2]
for s in iter(raw_input, "#"):
    digits = list(map(lambda x: pos[int(x)-1], s))
    def count_changes(lr):
        tmp, b = 0, digits[0]
        for f in digits[1:]:
            cond = (b < f if lr == 0 else b > f)
            if cond:
                tmp += 1
            else:
                lr ^= 1
            b = f
        return tmp
    print min(count_changes(lr) for lr in (0,1))