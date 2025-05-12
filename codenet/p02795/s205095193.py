H = int(input())
W = int(input())
N = int(input())

H = H
W = W
count = 0
paint = 0
while paint<N:
  if W>H:
    count +=1
    paint += W
    H-=1
  else:
    count +=1
    paint += H
    W -=1
else:
  print(count)