n=input()
n_sum=(sum(map(int,n)))

if int(n) % n_sum == 0:
  print("Yes")
else:
  print("No")