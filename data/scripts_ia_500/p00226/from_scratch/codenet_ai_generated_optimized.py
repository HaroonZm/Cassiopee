import sys

for line in sys.stdin:
    r, a = line.strip().split()
    if r == '0' and a == '0':
        break
    hit = sum(x == y for x, y in zip(r, a))
    # Count digits ignoring hits
    r_counts = [0]*10
    a_counts = [0]*10
    for i in range(4):
        if r[i] != a[i]:
            r_counts[int(r[i])] += 1
            a_counts[int(a[i])] += 1
    blow = sum(min(r_counts[i], a_counts[i]) for i in range(10))
    print(hit, blow)