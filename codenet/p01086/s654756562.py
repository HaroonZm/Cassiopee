flag=False

def dbg(a,b=None):
  print(a,b) if flag else None
  
def hante(arr,num):
  sum=0
  for i in range(len(arr)):
    sum+=arr[i]
    if sum==num:
      dbg((True,i),arr)
      return (True,i+1)
    if sum>num:
      dbg((False,None),arr)
      return (False,None)
  dbg((False,None),arr)
  return (False,None)

while True:
  n=int(input())
  if n==0:
    break;
  mojisuu=0
  w=["" for i in range(n)]
  for i in range(n):
    x=len(input())
    w[i]=x
    mojisuu+=x
  start=0
  while start<mojisuu:
    
    h1=hante(w[start:],5)
    if not h1[0]:
      start+=1
      continue
    h2=hante(w[start+h1[1]:],7)
    if not h2[0]:
      start+=1
      continue
    h3=hante(w[start+h1[1]+h2[1]:],5)
    if not h3[0]:
      start+=1
      continue
    h4=hante(w[start+h1[1]+h2[1]+h3[1]:],7)
    if not h4[0]:
      start+=1
      continue
    h5=hante(w[start+h1[1]+h2[1]+h3[1]+h4[1]:],7)
    if not h5[0]:
      start+=1
      continue
    break
  print(start+1)