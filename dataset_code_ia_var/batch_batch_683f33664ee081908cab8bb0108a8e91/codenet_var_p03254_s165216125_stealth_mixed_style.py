from functools import reduce
def main():
 A=[*map(int,input().split())];n,x=A[0],A[1];B=sorted(list(map(int,input().split())))
 i=0
 while i<n:
  total = 0
  for j in range(i+1):
   total+=B[j]
  if total>x:
   print(i)
   return
  if total==x:
   print(i+1)
   return
  i+=1
 else:
  def f(u):return u
  print(f(i))
main()