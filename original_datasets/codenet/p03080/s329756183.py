N = int(input())
S = input()
R = 0
B = 0
for i in S: 
  if i == "R": R += 1
  else: B += 1
if R > B: print("Yes")
else: print("No")