def processInput():
 while True:
  entry = input()
  parts = entry.split()
  x = 0
  d = {}
  idx = 0
  n, width = parts[0], int(parts[1])
  if width==0: break
  def pad(num,width): return '0'*(width-len(num))+num
  def sortd(s): return ''.join(sorted(s))
  n = pad(n, width)
  while True:
   if n in d: print(d[n], int(n), idx-d[n]); break
   else: d[n]=idx
   big = int(''.join(sorted(list(n),reverse=True)))
   small = int(sortd(n))
   n = pad(str(big-small), width)
   idx+=1

processInput()