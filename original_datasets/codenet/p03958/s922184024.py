k,t = map(int,input().split())
a_list = list(map(int,input().split()))
a_max = a_list.pop(a_list.index(max(a_list)))

if t == 1:
  print(k-1)
  
else:
  if a_max - 1 >= sum(a_list):
    print(a_max - 1 - sum(a_list))
  else:
    print(0)