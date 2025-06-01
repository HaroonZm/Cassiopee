import sys

for line in sys.stdin:
    if not line.strip():
        continue
    p, q = map(int, line.split())
    remainder = p % q

    digits = []
    seen = {}
    idx = 0
    start = -1
    while remainder != 0:
        if remainder in seen:
            start = seen[remainder]
            break
        seen[remainder] = idx
        remainder *= 10
        digits.append(str(remainder // q))
        remainder %= q
        idx += 1

    if remainder == 0:
        # finite decimal
        print("".join(digits))
    else:
        # recurring decimal
        non_recur = "".join(digits[:start])
        recur = "".join(digits[start:])
        print(non_recur + recur)
        print(" " * start + "^" * len(recur))