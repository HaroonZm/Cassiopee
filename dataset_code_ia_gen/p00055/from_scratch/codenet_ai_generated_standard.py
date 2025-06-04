import sys

for line in sys.stdin:
    a = line.strip()
    if not a:
        continue
    a = float(a)
    seq = [a]
    for i in range(1, 10):
        if (i+1) % 2 == 0:  # even index (1-based)
            seq.append(seq[-1] * 2)
        else:  # odd index (1-based)
            seq.append(seq[-1] / 3)
    print(sum(seq))