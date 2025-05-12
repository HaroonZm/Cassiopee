n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
max_sum = 0
for i in range(0,n):
  x = sum(a1[0:i+1]) + sum(a2[i:n+1])
  if max_sum  <= x:
    max_sum = x
print(max_sum)