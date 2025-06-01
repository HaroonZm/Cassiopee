t=int(raw_input())
for i in range(t):
 s=int(raw_input())
 print 'Case %s:' % str(i+1)
 for _ in range(10):
  s=int(str(s**2).zfill(8)[2:-2])
  print s