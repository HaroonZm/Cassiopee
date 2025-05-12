N, M = map(int, input().split())
AB = sorted([tuple(map(int, input().split())) for _ in range(N)])
count = 0
ans = 0
for a, b in AB:
    if count + b >= M:
        ans += a * (M - count)
        break
    else:
        ans += a * b
        count += b
print(ans)