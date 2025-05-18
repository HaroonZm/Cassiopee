A, B = map(int, input().split())
n = 1
while True:
  A_ = A * n
  if A_ % B == 0:
    print(A_)
    exit()
  n += 1