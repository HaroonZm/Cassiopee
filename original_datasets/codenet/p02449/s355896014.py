from itertools import permutations
n = int(input())
a = list(map(int, input().split()))
b = list(permutations(range(1, n+1)))
for i in range(len(b)):
  if b[i]==tuple(a):
    if i==0:
      pass
    else:
      print(" ".join(map(str, b[i-1])))
    print(" ".join(map(str, a)))
    if i==len(b)-1:
      pass
    else:
      print(" ".join(map(str, b[i+1])))
    break