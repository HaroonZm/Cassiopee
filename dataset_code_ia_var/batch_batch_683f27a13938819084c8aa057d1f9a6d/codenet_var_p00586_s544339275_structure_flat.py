import sys
for line in sys.stdin:
  parts = line.split()
  a = int(parts[0])
  b = int(parts[1])
  result = a + b
  print(result)