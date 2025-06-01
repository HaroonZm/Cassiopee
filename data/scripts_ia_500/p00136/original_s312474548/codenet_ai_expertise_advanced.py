from collections import Counter

n = int(input())
bins = [0]*6
thresholds = [165, 170, 175, 180, 185]

for _ in range(n):
    h = float(input())
    idx = next((i for i, t in enumerate(thresholds) if h < t), 5)
    bins[idx] += 1

for i, count in enumerate(bins, 1):
    print(f"{i}:{'*' * count}")