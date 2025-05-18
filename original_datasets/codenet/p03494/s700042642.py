N = int(input())
A = list(map(int, input().split()))

cnt = 0

while True:
  if all([i % 2 == 0 for i in A]):
    A = [i / 2 for i in A]
    cnt += 1
  else:
    break

print(cnt)