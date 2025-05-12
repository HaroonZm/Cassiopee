# /usr/bin/python

import sys

def machine(x,y):
  if x=='T' and y=='F':
    return 'F'
  else:
    return 'T'

N = int(input())
Pn = list(map(str, sys.stdin.readline().rstrip().split()))

for i in range(1, N):
  Pn[i] = machine(Pn[i-1], Pn[i])

print(Pn[-1])