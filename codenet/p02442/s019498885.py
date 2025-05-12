n = int(input())
A = input().replace(" ","")
m = int(input())
B = input().replace(" ","")
if n > m:
  for i in range(n - m):
    B += " "
elif m > n :
  for i in range(m - n):
    A += " "

if A >= B :
  print(0)
else:
  print(1)