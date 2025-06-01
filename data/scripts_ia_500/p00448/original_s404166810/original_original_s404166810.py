def v():
 for e in iter(input,'0 0'):
  r=int(e.split()[0])
  d=[int(''.join(x),2)for x in zip(*[input().split()for _ in[0]*r])]
  a=0
  for m in range(1<<~-r):
   t=0
   for s in d:
    c=bin(m^s).count('1')
    t+=c if c>r//2 else r-c
   if a<t:a=t
  print(a)
if'__main__'==__name__:v()