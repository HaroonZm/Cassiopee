from collections import Counter

while (n := int(input())):
    counts = Counter(int(input()) for _ in range(n))
    print(*(('*' * counts[i]) if counts[i] else '-' for i in range(10)), sep='\n')