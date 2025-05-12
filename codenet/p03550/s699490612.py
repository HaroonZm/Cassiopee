s1 = input()
s2 = input()

x, y, z = [int(i) for i in s1.split()]
l = [int(i) for i in s2.split()]

if x == 1:
  print(abs(z - l[x-1]))
else:
  if abs(z - l[x-1]) > abs(l[x-1] - l[x-2]):
    print(abs(z - l[x-1]))
  else:
    print(abs(l[x-1] - l[x-2]))