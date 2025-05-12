C = [0] * 6
for _ in [0] * int(raw_input()):
  a, b = map(int, raw_input().split('.'))
  if a<165: C[0]+=1
  else: C[(a-160)/5] += 1
for i in range(6):
  print '%d:%s' %(i+1, '*'*C[i])