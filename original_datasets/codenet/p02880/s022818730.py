n = int(input())

ck = 0
for i in range(1,10):
  if(n%i):
    continue
  else:
    if(n/i <= 9):
      ck = 1
      break
if(ck):
  print('Yes')
else:
  print('No')