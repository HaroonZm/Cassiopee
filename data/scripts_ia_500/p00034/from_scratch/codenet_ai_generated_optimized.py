import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    data = list(map(int, line.split(',')))
    l = data[:10]
    v1, v2 = data[10], data[11]
    total_len = sum(l)

    # proportion of track covered by each train at meeting time
    # meeting time t satisfies v1 * t + v2 * t = total_len => t = total_len / (v1 + v2)
    dist1 = v1 * total_len / (v1 + v2)

    cum = 0
    for i, length in enumerate(l, 1):
        prev_cum = cum
        cum += length
        if dist1 < cum:
            print(i)
            break
        elif dist1 == cum:
            print(i if i == 10 else i)
            break