N = int(input())
S = [input().strip() for i in range(N)]
T = input().strip()

lower = 1
upper = N + 1

for s in S:
    s_first = s.replace('?', 'a')
    s_last = s.replace('?', 'z')
    if T < s_first:
        upper -= 1
    if s_last < T:
        lower += 1

ans = ' '.join(map(str, range(lower, upper + 1)))
print(ans)