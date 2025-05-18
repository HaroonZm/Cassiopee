N = int(input())
S = input()
if N % 2 != 0:
  print("No")
  exit()
x = int(len(S) / 2)
y = S[0:x]
z = S[x:len(S)]
if y == z:
  print("Yes")
else:
  print("No")