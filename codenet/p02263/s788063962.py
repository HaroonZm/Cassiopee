def calc(E,A):
  if len(A) >= 2:
    a2 = int(A.pop())
    a1 = int(A.pop())
    if E == '*' :
      a3 = a1 * a2
    elif E == '+':
      a3 = a1 + a2
    elif E == '-':
      a3 = a1 - a2
    A.append(a3)
    

E = list(input().split())
a = []
for e in E:
  if (e == '+' or e == '-' or e == '*') :
    calc(e,a)
  else:
    a.append(e)

print(a[0])