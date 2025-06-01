from collections import Counter

while (n := int(input())):
    counts = Counter(int(input()) for _ in range(n))
    for i in range(10):
        print('*' * counts[i] or '-')