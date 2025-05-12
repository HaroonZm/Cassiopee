cnt = [0] * 4
for _ in range(3):
    a, b = tuple(map(int, input().split()))
    cnt[a-1] += 1
    cnt[b-1] += 1
for c in cnt:
    if c >= 3:
        print("NO")
        exit()
print("YES")