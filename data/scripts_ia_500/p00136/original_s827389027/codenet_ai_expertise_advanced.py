from collections import Counter

N = int(input())
thresholds = [165, 170, 175, 180, 185]

counts = Counter(min((i for i, t in enumerate(thresholds + [float('inf')]) if float(input()) < t)) for _ in range(N))

for i in range(6):
    print(f"{i+1}:{'*' * counts[i]}")