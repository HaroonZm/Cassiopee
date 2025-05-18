N = int(input())
X = list(map(int, input().split()))
ans = float('inf')

for i in range(100):
  temp = 0
  for j in range(N):
    temp += (X[j] - (i+1))**2
  if ans > temp:
    ans = temp

print(ans)