d = list(input())
a = 0
b = 0
c = 0
for i in range(3):
  if d[i] == "a":
    a = 1
  if d[i] == "b":
    b = 1
  if d[i] == "c":
    c = 1
    
    
if a*b*c == 1:
  print("Yes")
else:
  print("No")