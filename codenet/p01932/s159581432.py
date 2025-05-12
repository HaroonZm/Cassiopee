n, d = map(int, input().split())
lst = sorted([list(map(int, input().split())) for _ in range(n)]) + [[10 ** 20, 1]]
cnt = 0
time = 0
floor = 1
ans = 0
for i in range(n):
  t, f = lst[i]
  if f - floor > t - time or cnt >= d:
    print(-1)
    break

  ans += cnt * (t - time)
  cnt += 1
  time = t
  floor = f
  next_t, next_f = lst[i + 1]
  if time + (floor - 1) + (next_f - 1) <= next_t:
    ans += cnt * (floor - 1)
    cnt = 0
    time += floor - 1
    floor = 1
else:
  print(ans)