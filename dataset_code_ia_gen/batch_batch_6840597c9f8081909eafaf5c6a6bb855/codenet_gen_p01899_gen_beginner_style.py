N,d=map(int,input().split())
p=list(map(int,input().split()))
max_profit=0
for start in range(N):
  used=[False]*N
  used[start]=True
  res=-d
  cur=start
  while True:
    next_station=-1
    next_profit=0
    for i in range(N):
      if not used[i] and p[i]-d>next_profit:
        next_profit=p[i]-d
        next_station=i
    if next_profit<=0:
      break
    res+=next_profit
    used[next_station]=True
    cur=next_station
  res+=p[start]
  if res>max_profit:
    max_profit=res
if max_profit<=0:
  print("kusoge")
else:
  print(max_profit)