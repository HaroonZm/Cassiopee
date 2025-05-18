import sys
for line in sys.stdin.readlines():
  i = float(line)
  s = 0
  for x in range(5):
    s += i
    i *= 2
    s += i
    i /= 3
  print(s)