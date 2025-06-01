n = input()
a = [map(int, raw_input().split()) for i in range(n)]
for i in range(n):
  (a[i][0], a[i][1]) = (-a[i][1], a[i][0])
a.sort()
print a[0][1], -a[0][0]