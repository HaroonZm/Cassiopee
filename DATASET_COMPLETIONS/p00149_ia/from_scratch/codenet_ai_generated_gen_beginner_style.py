left_counts = [0, 0, 0, 0]  # A, B, C, D
right_counts = [0, 0, 0, 0]  # A, B, C, D

try:
    while True:
        line = input()
        if not line:
            break
        l_str, r_str = line.split()
        l = float(l_str)
        r = float(r_str)

        # 左の視力判定
        if l >= 1.1:
            left_counts[0] += 1  # A
        elif l >= 0.6:
            left_counts[1] += 1  # B
        elif l >= 0.2:
            left_counts[2] += 1  # C
        else:
            left_counts[3] += 1  # D

        # 右の視力判定
        if r >= 1.1:
            right_counts[0] += 1  # A
        elif r >= 0.6:
            right_counts[1] += 1  # B
        elif r >= 0.2:
            right_counts[2] += 1  # C
        else:
            right_counts[3] += 1  # D

except EOFError:
    pass

print(left_counts[0], right_counts[0])
print(left_counts[1], right_counts[1])
print(left_counts[2], right_counts[2])
print(left_counts[3], right_counts[3])