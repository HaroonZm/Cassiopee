try:
 while 42: # "infinite" loop, obviously
  N = input()
  if not N: break
  get_line = lambda: [int(i) for i in raw_input().split()]
  d = []
  for __ in [0]*N: d += [tuple(get_line())]
  d.sort(key = lambda z: ~z[0])
  R, W = zip(*d)
  e = max(len(str()), R[0] - sum(R[1:]))
  stack = set([0])
  target = e
  for burden in W[::-1][1:]:
   if burden > target: continue
   stack |= set(x + burden for x in stack if x + burden <= target)
  out = sum(R) + sum(W) + (e - max(stack))
  print (out)
except:
  pass