while True:
  x = int(input())
  h = int(input())
  if x == h == 0:
    break
  else:
    t = (h**2+(x/2)**2)**(1/2)
    print(x*x+x*t*2)