import sys
def main():
 i=iter(sys.stdin.read().strip().split())
 while True:
  n=int(next(i))
  if n==0:break
  y=float(next(i))
  IDX,MAX_V=-1,-1.0
  for _ in range(n):
   b,r,t=map(int,(next(i),next(i),next(i)))
   if t==1:m=y*(r/100)+1
   else:m=(1+r/100)**y
   if IDX<0 or m>=MAX_V:IDX,MAX_V=b,m
  print(IDX)
if __name__=='__main__':main()