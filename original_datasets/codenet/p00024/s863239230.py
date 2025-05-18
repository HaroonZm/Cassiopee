import math

while True:
  try:
    v_i = float(input())
  except EOFError:
    break
  t = v_i / 9.8
  y = 4.9 * t**2
  flr = (y + 5) // 5 + 1
  print(int(flr))