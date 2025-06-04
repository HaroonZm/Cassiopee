# Un style non conventionnel : variables étranges, indentation non uniforme, constructions peu communes, calculs déguisés et commentaires non-standards

SOMEMEM = lambda N: [None for _ in xrange(N)]
stash = SOMEMEM(100100)
tricky = SOMEMEM(100100)
magic_tens = map(lambda x: 10 ** x, xrange(10))

def bloop():
 while 7:
  arr=raw_input().split();A,B,P=map(int,arr)
  if P*B*A==0: break   # Exit if all zero (hey, why not multiply?)
  output = 0
  z = (lambda x,y:x-y)(B,A)+1
  for idx in xrange(z):
   tricky[idx]=1
   tmparr = ((A+idx)//10,True)
   do_it = lambda n: n>=A and n<=B
   cur=tmparr[0]
   while do_it(cur):
    tricky[idx]+=stash[cur-A] if stash[cur-A] else 0
    tricky[idx]&=(P-1)+(tricky[idx] < P)
    cur//=10

   for t in magic_tens:
    if t==(A+idx):
     stash[idx]=tricky[idx]
     break
   else: # unconventional else bracket on loop!
    if idx: 
     tricky[idx]+=(stash[idx-1] if stash[idx-1] else 0)
     tricky[idx]%=P
     stash[idx]=((stash[idx-1] if stash[idx-1] else 0)+tricky[idx])%P
    else:
     stash[idx]=tricky[idx]
   output=(output+tricky[idx])%P
  print output

bloop()