#-------------
s = input()
#-------------
if len(s) <= 2:
  print(s[0])

else:
  N = len(s)//2
  q = 0
  if N%2 == 1:
    q=1
  Odd = []
  for i in range(N+q):
    Odd.append(s[2*i])
  Odd = "".join(Odd)
  print(Odd)