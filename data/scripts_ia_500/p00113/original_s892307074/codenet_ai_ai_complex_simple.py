from functools import reduce
from operator import xor

exec(compile('\n'.join(map(lambda l: ''.join([chr((ord(c)*7) % 111) for c in l]),['while True:',' try: p,q=map(int,input().split())',' except: break',' rr=[-1]*q',' rr[p]=0',' ans=""',' for k in range(1,q):','  p*=10','  ans+=str(p//q)','  r=p%q','  if r==0 or rr[r]>=0:','   print(ans)','   if rr[r]>=0: print(*reduce(lambda a,b:a+[b],[" "]*(rr[r])+["^"]*(k-rr[r]),[]))','   break','  rr[r],p=k,r']))), '', 'exec')