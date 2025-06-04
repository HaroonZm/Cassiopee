from collections import Counter

N, L = map(int, input().split())
words = [input() for _ in range(N)]

count = Counter(words)
left_parts = []
middle = ""
for w in sorted(count.keys()):
    rev = w[::-1]
    if w == rev:
        pairs = count[w] // 2
        if pairs > 0:
            left_parts.extend([w] * pairs)
            count[w] -= pairs * 2
    else:
        if w < rev and rev in count:
            pairs = min(count[w], count[rev])
            if pairs > 0:
                left_parts.extend([w] * pairs)
                count[w] -= pairs
                count[rev] -= pairs

for w in sorted(count.keys()):
    if w == w[::-1] and count[w] > 0:
        middle = w
        break

right_parts = [w[::-1] for w in reversed(left_parts)]
print("".join(left_parts) + middle + "".join(right_parts))