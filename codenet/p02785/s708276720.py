N, K = map(int, input().split())
H = list(map(int, input().split()))

if N <= K:
  print("0")
  exit()

ans = 0

def quicksort(a):
  if len(set(a)) < 2:
    return a
  left = []
  center = a.pop(0)
  right = []
  for i in a:
    if i > center:
      right.append(i)
    else:
      left.append(i)
  left = quicksort(left)
  right = quicksort(right)
  left.append(center)
  left.extend(right)
  return left

H = quicksort(H)

for i in range(N-K):
  ans += H[i]

print(ans)