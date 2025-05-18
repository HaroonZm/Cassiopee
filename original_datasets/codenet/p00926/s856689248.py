import sys
reader=(token for line in sys.stdin for token in line.split())

while 1:
  try:
    n=int(next(reader))
    m=int(next(reader))
  except: break

  a=[1]*(n+1)
  for i in range(m):
    c=int(next(reader))-1
    d=int(next(reader))-1
    for i in range(c,d):
      a[i]=3
  print(sum(a))