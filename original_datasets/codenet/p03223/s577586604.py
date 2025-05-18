N=int(input())
A=[int(input())for _ in range(N)]

A=sorted(A)
B=A[:]

ans=0
#小さいのが真ん中
top=A[0]
bottom=A[0]
tmp=0
turn=True
del A[0]
while  A:
  if len(A)==1:
    tmp+=max(abs(top-A[0]),abs(bottom-A[0]))
    break
    pass
  if turn:
    a,b=A[-2],A[-1]
  else:
    a,b=A[0:2]
    
  if abs(a-bottom)+abs(b-top)<abs(a-top)+abs(b-bottom):
    a,b=b,a
  tmp+=abs(a-bottom)+abs(b-top)
  bottom,top=a,b
  if turn:
    del A[-1]
    del A[-1]
  else:
    del A[0]
    del A[0]
  turn=not turn

ans=tmp
A=B
top=A[-1]
bottom=A[-1]
tmp=0
del A[-1]
turn = True
while  A:
  #print("center big:tmp: ", tmp)
  if len(A)==1:
    tmp+=max(abs(top-A[0]),abs(bottom-A[0]))
    break
    pass
  if turn:
    a,b=A[0],A[1]
  else:
    a,b=A[-1],A[-2]
    
  if abs(a-bottom)+abs(b-top)<abs(a-top)+abs(b-bottom):
    a,b=b,a
  tmp+=abs(a-bottom)+abs(b-top)
  bottom,top=a,b
  if turn:
    del A[0] 
    del A[0]
  else:
    del A[-1]
    del  A[-1]
  turn= not turn

ans=max(ans,tmp)
print(ans)