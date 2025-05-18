N,X=[int(x) for x in str(input()).split()]

num=[1]
for i in range(1,51):
  num.append(2*num[-1]+3)

full=[1]
for i in range(1,51):
  full.append(2*full[-1]+1)

def f(n,x):
  if n==0:
    return(1)
  else:
    if x==1:
      return 0
    elif x<=num[n-1]+1:
      return f(n-1,x-1)
    elif x==num[n-1]+2:
      return 1+full[n-1]
    elif x==num[n]:
      return 1+2*full[n-1]
    else:
      return 1+full[n-1]+f(n-1,x-2-num[n-1])
    

print(f(N,X))