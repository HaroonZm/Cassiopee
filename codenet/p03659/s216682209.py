n = int(input())
a = list(map(int, input().split()))
sum_a = [0]
for i in range(n):
  sum_a.append(sum_a[-1] + a[i])
del sum_a[0]
del sum_a[-1]
total = sum(a)
for i in range(n - 1):
  sum_a[i] = abs(total / 2 - sum_a[i])
print(int(min(sum_a) * 2))