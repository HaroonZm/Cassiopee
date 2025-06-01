from collections import Counter
while (n := int(input())) != 0:
    counts = Counter(int(input()) for _ in range(n))
    for i in range(10):
        print('*' * counts[i] if counts[i] else '-')