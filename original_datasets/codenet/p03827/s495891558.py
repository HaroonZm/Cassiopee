N = int(input())
S = input()

x = 0
ans = 0
for c in S:
    x += 1 if c == 'I' else -1
    ans = max(ans, x)

print(ans)