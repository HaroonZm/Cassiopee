x=[]
y=[]
for _ in [0]*3:
  a = sorted([raw_input().split()[::-1] for _ in [0]*8])
  x += a[0:2]
  y += a[2:4]
x += sorted(y)[0:2]

for e in x:
  print " ".join(e[::-1])