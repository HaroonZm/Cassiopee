import math
 
rad = math.radians(60)
 
class coordinates:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
def koch(n, a, b):
  if n == 0:
    return
  s = coordinates((2.0*a.x + b.x)/3.0, (2.0*a.y + b.y)/3.0)
  t = coordinates((a.x + 2.0*b.x)/3.0, (a.y + 2.0*b.y)/3.0)
  ux = (t.x - s.x)*math.cos(rad) - (t.y - s.y)*math.sin(rad) + s.x
  uy = (t.x - s.x)*math.sin(rad) + (t.y - s.y)*math.cos(rad) + s.y
  u = coordinates(ux, uy)
   
  koch(n-1, a, s)
  print  s.x, s.y
  koch(n-1, s, u)
  print  u.x, u.y
  koch(n-1, u, t)
  print  t.x, t.y
  koch(n-1, t, b)
   
n = input()
   
p1 = coordinates(0.0, 0.0)
p2 = coordinates(100.0, 0.0)
   
print p1.x, p1.y
koch(n, p1, p2)
print p2.x, p2.y