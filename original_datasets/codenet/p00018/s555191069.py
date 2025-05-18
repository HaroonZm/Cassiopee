a = map(int,raw_input().split())
a.sort()
a.reverse()
for i in range(len(a)):
  print a[i],