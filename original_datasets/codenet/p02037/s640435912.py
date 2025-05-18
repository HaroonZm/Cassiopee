# /usr/bin/python

import sys

h,w = map(int, input().split())
a,b = map(int, input().split())

print(h*w - (h//a*a) * (w//b*b))