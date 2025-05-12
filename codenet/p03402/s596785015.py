# aaaaabbbbb
# a_a_ab_b_b
# aaaaabbbbb
# a_a_ab_b_b
# aaaaabbbbb

# 51x41 → 25x20の_がくり抜ける
# 51x82

H = 24
W = 49
#H = 3
#W = 4
import numpy as np
X = np.full((W+W+1,2*(H+H+1)),'.',dtype='U1')
A,B = map(int,input().split())

# view
left = X[:,:H+H+1]
right = X[:,H+H+1:]
right[:] = '#'

for symbol,n,view in [['#',B-1,left],['.',A-1,right]]:
  q,r = n//H,n%H
  for i in range(q):
    view[2*i+1,1::2] = symbol
  view[2*q+1,1:1+2*r:2] = symbol

print(2*W+1,4*H+2)
for row in X:
  print(''.join(row))