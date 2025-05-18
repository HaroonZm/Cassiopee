while True:
  s = input()
  if not s:
    break
  for i in range(9):
    s -= input()
  print s