l = int(input())
n = int(input())
mom = 0
for _ in range(n):
  x, w = map(int, input().split())
  mom += x * w

weight = []
while mom:
  if mom < 0:
    add_weight = min(-mom, 50000)
    mom += add_weight
    weight.append((1, add_weight))
  elif mom > 0:
    add_weight = min(mom, 50000)
    mom -= add_weight
    weight.append((-1, add_weight))

print(len(weight))
for t in weight:
  print(*t)