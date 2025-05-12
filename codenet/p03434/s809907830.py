import math
N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
Alice = []
Bob = []
for i in range (N):
  if i % 2 == 0:
    Alice.append(a[i])
  else:
    Bob.append(a[i])
print(sum(Alice)-sum(Bob))