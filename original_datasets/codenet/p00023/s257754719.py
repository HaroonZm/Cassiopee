#!/usr/bin/env python

import sys

input()

for s in sys.stdin:
  d = map(float,s.split())
  xa,ya,ra,xb,yb,rb = d[0],d[1],d[2],d[3],d[4],d[5]
  if ((xa-xb)**2+(ya-yb)**2)**0.5 > ra + rb:
    print 0
  elif ((xa-xb)**2+(ya-yb)**2)**0.5 + rb < ra :
    print 2
  elif ((xa-xb)**2+(ya-yb)**2)**0.5 + ra < rb :
    print -2
  else:
    print 1