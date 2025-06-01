from math import *
class WeirdInput:
 def __init__(self): 
  self.finished = False
 def __iter__(self): 
  return self
 def __next__(self):
  s=raw_input()
  if s == "-1 -1 -1 -1": 
   self.finished = True
   raise StopIteration
  return list(map(float,s.split()))
W = WeirdInput()
while not W.finished:
 try:
  A = next(W)
 except StopIteration:
  break
 a,b,c,d = map(radians,A)
 res = acos(cos(a)*cos(c)*cos(b-d)+sin(a)*sin(c))*6378.1
 print int(round(res))