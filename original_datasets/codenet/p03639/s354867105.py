from collections import Counter

N = int(input())
c = Counter(map(lambda x: int(x) % 4, input().split()))
print('Yes') if sum([c[1], c[2] > 0, c[3]]) <= c[0] + 1 else print('No')