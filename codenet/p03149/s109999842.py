n = list(map(int, input().split()))
n.sort()
val = 1000*n[0]+100*n[3]+10*n[2]+n[1]
if(val == 1974):
  print("YES")
else:
  print("NO")