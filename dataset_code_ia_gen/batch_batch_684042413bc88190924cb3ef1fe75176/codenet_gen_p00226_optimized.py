import sys

for line in sys.stdin:
    r, a = line.strip().split()
    if r == '0' and a == '0':
        break

    hit = sum(rc == ac for rc, ac in zip(r, a))
    hit_positions = {i for i, (rc, ac) in enumerate(zip(r, a)) if rc == ac}
    r_counts = {}
    a_counts = {}
    for i in range(4):
        if i not in hit_positions:
            r_counts[r[i]] = r_counts.get(r[i], 0) + 1
            a_counts[a[i]] = a_counts.get(a[i], 0) + 1
    blow = sum(min(r_counts.get(d, 0), a_counts.get(d, 0)) for d in r_counts)
    print(hit, blow)