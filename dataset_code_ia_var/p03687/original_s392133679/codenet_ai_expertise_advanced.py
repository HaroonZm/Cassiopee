from collections import defaultdict

s = input()
n = len(s)
ans = n // 2

positions = defaultdict(list)
for i, c in enumerate(s):
    positions[c].append(i)

for c in (chr(i) for i in range(97, 123) if c in positions):
    pos = positions[c]
    chunks = [pos[0], n - 1 - pos[-1]]
    chunks += [pos[i] - pos[i-1] - 1 for i in range(1, len(pos))]
    haba = max(chunks)
    ans = min(ans, haba)

print(ans)