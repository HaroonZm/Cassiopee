x,a,b = map(int,input().split())

kyori1 = max(x,a) - min(x,a)
kyori2 = max(x,b) - min(x,b)

if kyori1 < kyori2:
  print('A')
else:
  print('B')