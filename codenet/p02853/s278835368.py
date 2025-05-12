X, Y = map(int, input().split())

total = 0

if X == 1:
  total += 300000
elif X == 2:
  total += 200000
elif X == 3:
  total += 100000
  
if Y == 1:
  total += 300000
elif Y == 2:
  total += 200000
elif Y == 3:
  total += 100000

if X == 1 and Y == 1:
  total += 400000

print(total)