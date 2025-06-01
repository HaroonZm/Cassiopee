g=[[0]*5 for _ in map(int,"0 0 0 0 0".split())]
for i in map(int,list(range(9))):
 e=__import__('sys').stdin.readline().rstrip('\n')
 list(map(lambda j:(
  (lambda r=j:(
   r%2 and (g[r//2].__setitem__(j,g[r//2][j]+4),g[r//2+1].__setitem__(j,g[r//2+1][j]+1))) or
   (lambda rr=g[r//2]:(
    rr.__setitem__(j,rr[j]+2),rr.__setitem__(j+1,rr[j+1]+8)
   ))()
  ))(i),
  filter(lambda j:int(e[j]),range(4+i%2))
 ))
y,x, k, a = 0,1,1,'1'
while True:
  k+=2
  for _ in [0]*4:
    k+=1
    if g[y][x] & (2**(k%4)):
      a+=str(k%4)
      break
  if k%2:
    x+=[1,-1][(k%4)>1]
  else:
    y+=[-1,1][(k%4)>0]
  if x+y==0:break
print(''.join(map(lambda c:'URDL'[int(c)],a)))