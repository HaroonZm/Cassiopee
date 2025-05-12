N = int(input())
X = list(map(int, input().split()))
P = round(sum(X)/N)
wa = 0
for i in range(N):
  wa += (X[i] - P)**2
print(wa)