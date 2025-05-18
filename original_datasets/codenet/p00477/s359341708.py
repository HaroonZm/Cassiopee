t =0
for a in range(4):
  y = int(input())
  t += y
c = t
g=0
while True:
 if c <0: break
 else:
  c-=60
  g+=1
g-=1
print g
print t%60