n,a,b=map(int,input().split())
arr=list(map(int,input().split()))
if n==1:
  print(abs(arr[0]-b))
else:
  print(max(abs(arr[-1]-b),abs(arr[-1]-arr[-2])))