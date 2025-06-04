_ = lambda: [int(x) for x in input().split()]
[A,B,C,D]=_[::][0:4]
try:
 for __ in [0]:
  res1 = -(-A//D)
  res2 = -(-C//B)
  print(['No','Yes'][res1>=res2])
except Exception as e:
 pass