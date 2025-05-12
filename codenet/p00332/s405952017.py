def wa(y):
  if y <= 1911:
    return "M" + str(y - 1867)
  elif y  <= 1925:
    return "T" + str(y - 1911)
  elif y <= 1988:
    return "S" + str(y - 1925)
  else:
    return "H" + str(y - 1988)
def sei(e, y):
  if e == 1:
    return y + 1867
  elif e == 2:
    return y + 1911
  elif e == 3:
    return y + 1925
  else:
    return y + 1988 
e, y = map(int, input().split())
if e == 0:
  print(wa(y))
else:
  print(sei(e, y))