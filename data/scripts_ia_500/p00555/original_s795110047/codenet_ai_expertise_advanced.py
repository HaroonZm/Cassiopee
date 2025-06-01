N, M, D = map(int, input().split())
S = [input() for _ in range(N)]

def count_segments(lines):
    return sum(sum(1 for _ in range(0, len(row) - D + 1) if all(c == '.' for c in row[i:i+D])) for row in lines)

ans = 0

# Horizontal count
for row in S:
    count = 0
    for c in row:
        count = count + 1 if c == '.' else 0
        ans += count >= D

# Vertical count
for col in zip(*S):
    count = 0
    for c in col:
        count = count + 1 if c == '.' else 0
        ans += count >= D

print(ans)