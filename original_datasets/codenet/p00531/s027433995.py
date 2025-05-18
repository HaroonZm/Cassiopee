a = []
for i in range(5):
  a.append(int(input()))

x = a[0] * a[4]
y = a[1] + max(a[4] - a[2], 0) * a[3]

print(min(x, y))