import sys

rides = [4,4,2,2,1,1,1,1]

for line in sys.stdin:
    if not line.strip():
        continue
    p = list(map(int, line.split()))
    if len(p) != 8:
        continue

    best_unseated = float('inf')
    best_pattern = None

    for shift in range(8):
        assigned = [rides[(i+shift)%8] for i in range(8)]
        unseated = 0
        for passengers, capacity in zip(p, assigned):
            unseated += max(0, passengers - capacity)
        if unseated < best_unseated:
            best_unseated = unseated
            best_pattern = assigned
        elif unseated == best_unseated:
            # Compare patterns as 8-digit numbers
            current_num = int(''.join(map(str, assigned)))
            best_num = int(''.join(map(str, best_pattern)))
            if current_num < best_num:
                best_pattern = assigned

    print(' '.join(map(str, best_pattern)))