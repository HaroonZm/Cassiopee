from collections import Counter

n, l = map(int, input().split())
words = [input() for _ in range(n)]
count = Counter(words)

left, middle = [], ''

for word in sorted(count.keys()):
    rev = word[::-1]
    if word == rev:
        pairs = count[word] // 2
        left.extend([word] * pairs)
        count[word] -= 2 * pairs
        if count[word] and len(word) > len(middle):
            middle = word
    elif count[word] and count[rev]:
        pairs = min(count[word], count[rev])
        left.extend([word] * pairs)
        count[word] -= pairs
        count[rev] -= pairs

result = ''.join(left) + middle + ''.join(left[::-1])
print(result)