from collections import Counter
n = int(input())
counter1 = Counter(input())
counter2 = Counter(input())
values1 = [0] * (26 - len(counter1)) + sorted(counter1.values())
values2 = [0] * (26 - len(counter2)) + sorted(counter2.values())
print(sum([abs(i - j) for i, j in zip(values1, values2)]) // 2)