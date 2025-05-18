N, A, B = map(int, input().split())
r = 0
for i in range(N):
  t = int(input())
  if not A <= t < B:
    r += 1
print(r)