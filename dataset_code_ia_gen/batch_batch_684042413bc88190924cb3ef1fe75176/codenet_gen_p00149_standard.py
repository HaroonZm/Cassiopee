import sys

def classify(v):
    if v >= 1.1:
        return 0
    elif v >= 0.6:
        return 1
    elif v >= 0.2:
        return 2
    else:
        return 3

left_counts = [0]*4
right_counts = [0]*4

for line in sys.stdin:
    if line.strip():
        l, r = map(float, line.split())
        left_counts[classify(l)] += 1
        right_counts[classify(r)] += 1

for i in range(4):
    print(left_counts[i], right_counts[i])