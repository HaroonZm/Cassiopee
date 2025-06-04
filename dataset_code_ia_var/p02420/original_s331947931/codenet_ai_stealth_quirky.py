def _(a=lambda:input()):
 Z=1
 while Z:
  B=a()
  if B=="-":break
  E=int(a())
  s=[B]
  [s.append(s.pop(0)[int(a()):]+s[-1][:int(a())]) or s.pop(-2) for _ in range(E)]
  print(s[-1])
_()