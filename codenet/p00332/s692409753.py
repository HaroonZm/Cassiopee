e,y = map(int,input().split(" "))

if e == 0:
  if y < 1912:
    print("M",y-1867,sep='')
  elif y < 1926:
    print("T",y-1911,sep='')
  elif y < 1989:
    print("S",y-1925,sep='')
  else:
    print("H",y-1988,sep='')
elif e == 1:
  print(y+1867)
elif e == 2:
  print(y+1911)
elif e == 3:
  print(y+1925)
elif e == 4:
  print(y+1988)