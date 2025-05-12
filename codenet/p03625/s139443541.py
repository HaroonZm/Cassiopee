n = int(input())
a = list(map(int,input().split()))
dic = {}
for i in a:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1
    
first = 0
second = 0
for i,j in dic.items():
  if j >= 2:
    if i > first :
      second = first
      first = i
    elif i > second:
      second = i
      
  if j >= 4:
    if i > first :
      second = first
      first = i
    elif i > second:
      second = i
  
print(first*second)