while True:
  n = int(input())
  if n == 0:
    break
  f = [0] * 10
  for i in range(n):
    f[int(input())] += 1
  for i in range(10):
    if f[i] == 0:
      print('-')
    else:
      print('*'*f[i])