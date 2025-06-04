import sys

def read_ints():
  return list(map(int, sys.stdin.readline().split()))

L = []
for _ in range(2):
    nums = read_ints()
    L.append(sum(nums))

if L[0] >= L[1]:
  print(L[0])
else:
  print(L[1])