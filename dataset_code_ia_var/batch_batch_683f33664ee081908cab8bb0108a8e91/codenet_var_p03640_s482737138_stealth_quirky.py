import sys as s
H,W=[*map(int,s.stdin.readline().split())]
N=int(s.stdin.readline())
A=[int(x)for x in s.stdin.readline().split()]
_direction=-1
bucket=[]
idx=0
while idx<N:
 for k in range(A[idx]):
  if len(bucket)==W:
   print(*(bucket[::-1] if _direction<0 else bucket))
   bucket.clear()
   _direction*=-1
  if _direction<0:
   bucket.append(idx+1)
  else:
   bucket.insert(0,idx+1)
 idx+=1
if bucket:
 print(*(bucket[::-1] if _direction<0 else bucket))