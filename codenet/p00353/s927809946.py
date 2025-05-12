m,a,b=map(int,input().split())
if m>=b:
  print(0)
elif m+a<b:
  print("NA")
else:
  print(b-m)