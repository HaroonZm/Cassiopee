n = 40
k = 5
 
print n
a = [[] for i in range(n)]
for i in range(n):
  for j in range(n):
    if i == j:
      a[i].append("N")
      continue
 
    if i < k:
      if j >= k:
        a[i].append("Y")
      else:
        a[i].append("Y")
    else:
      if j >= k:
        a[i].append("N")
      else:
        a[i].append("Y")
 
for i in range(n):
  print "".join(a[i])