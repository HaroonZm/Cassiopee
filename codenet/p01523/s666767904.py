n, m = map(int, input().split())
pros = sorted([list(map(int, input().split())) for _ in range(m)])
index = 0
covered = 0
right = 0
ans = 0
while True:
  a, b = pros[index]
  if a > covered + 1:
    if covered == right:
      print("Impossible")
      break
    covered = right
    ans += 1
    continue
  else:
    right = max(right, b)
    index += 1

  if covered == n:
    print(ans)
    break

  if index == m:
    covered = right
    ans += 1
    print(ans if covered == n else "Impossible")
    break