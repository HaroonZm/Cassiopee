mylist = set([i for i in map(str,input().split())])

if '1' in mylist and '9' in mylist and '7' in mylist and '4' in mylist:
  print("YES")
else:
  print("NO")