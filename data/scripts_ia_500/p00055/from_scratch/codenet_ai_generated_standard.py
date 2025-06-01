import sys

for line in sys.stdin:
    a = line.strip()
    if not a:
        continue
    a = float(a)
    seq = [a]
    for i in range(1, 10):
        if (i + 1) % 2 == 0:
            seq.append(seq[-1] * 2)
        else:
            seq.append(seq[-1] / 3)
    print(sum(seq))