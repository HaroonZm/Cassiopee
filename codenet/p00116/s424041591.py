while 1:
  h,w = map(int, raw_input().split())
  if h==w==0: break
  H = range(h)
  C = [0]*(h+1)
  M = C[:]
  a=[0]*w
  for i in H:
    x = raw_input()
    b=[0]*w
    sp=-1
    C = [-1]*(h+1)
    for j in range(w):
      if x[j]=="*":
        c=0
      elif x[j]==".":
        c=a[j]+1
      b[j]=c
      if c>sp:
        C[sp+1:c+1]=[j]*(c-sp)
      elif c<sp:
        for k in range(c+1,sp+1):
          M[k]=max(M[k],j-C[k])
          C[k]=-1
      sp=c
    for k in range(1,sp+1):
      if C[k]>=0:
        M[k]=max(M[k],w-C[k])
    a=b[:]
  s=max([a*b for a,b in zip(M,range(h+1))])
  print s