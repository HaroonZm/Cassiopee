n, m = map(int, input().split())
point = []
for _ in range(m):
    atari, hazure = map(int, input().split())
    point.append([atari, hazure])
point.sort(reverse=True)
ans = 0
for [atari, _] in point[:m-1]:
    if atari >= n:
        continue
    else:
        ans += n - atari
print(ans)