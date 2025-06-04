from collections import Counter
N, L = map(int, input().split())
words = [input() for _ in range(N)]
count = Counter(words)
used_left, used_right = [], []
center = ''
for w in sorted(count):
    rev = w[::-1]
    if w == rev:
        pairs = count[w] // 2
        used_left.extend([w] * pairs)
        count[w] -= pairs * 2
for w in sorted(count):
    rev = w[::-1]
    if w < rev and count[w] > 0 and count[rev] > 0:
        pairs = min(count[w], count[rev])
        used_left.extend([w] * pairs)
        count[w] -= pairs
        count[rev] -= pairs
for w in sorted(count):
    if count[w] > 0 and w == w[::-1]:
        center = w
        break
used_right = [w[::-1] for w in used_left[::-1]]
res = ''.join(used_left) + center + ''.join(used_right)
print(res) if res else print()