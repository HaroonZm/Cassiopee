while True:
  n,r = tuple(map(int,input().split()))
  if n==0 and r==0:
    break
  l = [n-i for i in range(n)]
  for i in range(r):
    p,c = tuple(map(int,input().split()))
    l1 = [l[i] for i in range(p-1,p+c-1)]
    l2 = [l[i] for i in range(0,p-1)]
    l3 = l1+l2
    for i in range(p+c-1):
      l[i] = l3[i]
  print(l[0])