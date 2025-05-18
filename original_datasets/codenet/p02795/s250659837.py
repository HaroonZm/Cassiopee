H = int(input())
W = int(input())
N = int(input())
if W >= H:
  if N % W == 0:
    print(N//W)
  else:
    print(N//W+1)
else:
  if N % H == 0:
    print(N//H)
  else:
    print(N//H+1)