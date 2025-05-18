while True:
  s1 = list(input())
  if s1 == ["-"]:
    break
  s2 = list(input())
  s1.reverse()
  s2.reverse()
  under = list(input())
  under.reverse()
  right = []
  center = s2.pop()
  while s1 or s2:
    if under and center == under[-1]:
      center = s1.pop()
      under.pop()
    else:
      right.append(center)
      center = s2.pop()
  if not under:
    right.append(center)
  print("".join(right))