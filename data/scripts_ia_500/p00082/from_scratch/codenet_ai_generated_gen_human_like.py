import sys

# 定義された乗り物
rides = [4, 4, 2, 2, 1, 1, 1, 1]

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    p = list(map(int, line.split()))
    if len(p) != 8:
        continue

    min_unboarded = None
    best_pattern = None

    # 0から7までのずらしを試す
    for shift in range(8):
        unboarded = 0
        pattern = []
        for i in range(8):
            ride_type = rides[(i + shift) % 8]
            waiting = p[i]
            unboarded += max(0, waiting - ride_type)
            pattern.append(ride_type)
        # 最小のunboardedを更新
        if (min_unboarded is None) or (unboarded < min_unboarded):
            min_unboarded = unboarded
            best_pattern = pattern
        elif unboarded == min_unboarded:
            # Vを比較：８桁の整数として比較
            current_v = int(''.join(map(str, best_pattern)))
            new_v = int(''.join(map(str, pattern)))
            if new_v < current_v:
                best_pattern = pattern
    print(' '.join(map(str, best_pattern)))