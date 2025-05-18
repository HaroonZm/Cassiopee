a,b,c,k=map(int,input().split())

if(k%2==0):
  if abs(a-b)<10**18:
    print(a-b)
  else:
    print("Unfair")
else:
  if abs(a-b)<10**18:
    print(b-a)
  else:
    print("Unfair")