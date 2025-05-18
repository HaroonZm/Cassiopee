x, y, z = map(int, input().split(' '))

if x % (y+z) >= z:
  print(int(x / (y + z)))
else:
  print(int(x / (y + z)) - 1)