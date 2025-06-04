try:
 while 1:
  z = raw_input().split()
  if len(z)!=2: continue
  a,b=[int(s) for s in z]
  if not (a|b):break
  counter=[0]
  def tick():counter[0]+=1
  def check(i,j,k): return i+j+k==b
  map(lambda i:map(lambda j:map(lambda k:tick() if check(i,j,k) else None,range(j+1,a+1)),range(i+1,a+1)),range(1,a+1))
  print counter[0]
except EOFError: pass