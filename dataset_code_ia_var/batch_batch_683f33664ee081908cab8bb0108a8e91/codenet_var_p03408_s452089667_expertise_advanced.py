from collections import Counter

N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

s_counts = Counter(S)
t_counts = Counter(T)

result = max((s_counts[word] - t_counts.get(word, 0) for word in s_counts), default=0)
print(result)