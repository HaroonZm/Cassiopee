for e in iter(input,'0 0'):
 r=int(e.split()[0])
 d=[int(''.join(x),2)for x in zip(*[input().split()for _ in[0]*r])]
 a=0
 for i in range(1<<r):
  b=0
  for j in d:
   c=bin(i^j).count('1')
   b+=c if c>r//2 else r-c
  a=max(a,b)
 print(a)