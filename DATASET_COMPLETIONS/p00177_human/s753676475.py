from math import *
while 1:
  A = map(float,raw_input().split())
  if A == [-1]*4: break
  a,b,c,d = map(radians, A)
  print int(round(acos(cos(a)*cos(c)*cos(b-d)+sin(a)*sin(c))*6378.1))