import sys

h,w=map(int,input().split())

ans=10**10

S=[]

if h%3==0 or w%3==0:
  print(0)
  sys.exit()

for h1 in [h//3,(h//3)+1]:
  if ((h-h1)*w)%2==0:
    S.append([h1*w,((h-h1)*w)//2,((h-h1)*w)//2])
  else:
    S.append([h1*w,((h-h1)//2)*w,((h-h1)//2+1)*w])
    S.append([h1*w,(w//2)*(h-h1),(w//2+1)*(h-h1)])

for w1 in [w//3,(w//3)+1]:
  if ((w-w1)*h)%2==0:
    S.append([w1*h,((w-w1)*h)//2,((w-w1)*h)//2])
  else:
    S.append([w1*h,((w-w1)//2)*h,((w-w1)//2+1)*h])
    S.append([w1*h,(h//2)*(w-w1),(h//2+1)*(w-w1)])

for si in S:
  ans=min(ans,max(si)-min(si))

print(ans)