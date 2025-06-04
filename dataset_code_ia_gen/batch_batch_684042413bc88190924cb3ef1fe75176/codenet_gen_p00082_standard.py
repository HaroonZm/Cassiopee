vehicles = [4, 4, 2, 2, 1, 1, 1, 1]
import sys
for line in sys.stdin:
    p = list(map(int, line.split()))
    if len(p) != 8:
        continue
    best_unmatched = None
    best_pattern = None
    for shift in range(8):
        unmatched = 0
        for i in range(8):
            cap = vehicles[(i + shift) % 8]
            if p[i] > cap:
                unmatched += p[i] - cap
        if best_unmatched is None or unmatched < best_unmatched:
            best_unmatched = unmatched
            best_pattern = [(vehicles[(i + shift) % 8]) for i in range(8)]
        elif unmatched == best_unmatched:
            old_val = int(''.join(map(str, best_pattern)))
            new_val = int(''.join(str(vehicles[(i + shift) % 8]) for i in range(8)))
            if new_val < old_val:
                best_pattern = [(vehicles[(i + shift) % 8]) for i in range(8)]
    print(*best_pattern)