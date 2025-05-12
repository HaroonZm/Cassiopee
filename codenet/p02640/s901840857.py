X, Y = map(int, input().split())

for i in range(0, X+1):
  kame = 2 * i
  ashi = Y - kame
  if ashi % 4 == 0:
    if ashi // 4 == X-i:
      print("Yes")
      exit()

print("No")