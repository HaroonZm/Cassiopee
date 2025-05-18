a,b,c,x,y = map(int,input().split())

pricemin = a*x + b*y
if x>y:
  for i in range(x+1):
    m = max(y-i,0)
    price = a*(x-i) + b*m + c*2*i
    if price<pricemin:
      pricemin = price
else:
  for i in range(y+1):
    m = max(x-i,0)
    price = a*m + b*(y-i) + c*2*i
    if price<pricemin:
      pricemin = price
print(pricemin)