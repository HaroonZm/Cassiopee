def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b ,a%b)

def lcm(a,b):
  return a*b / gcd(a,b)

while True:
  try:
    a = map(int,raw_input().split())
    a,b = a[0],a[1]
    print gcd(a,b)
  except EOFError:
    break