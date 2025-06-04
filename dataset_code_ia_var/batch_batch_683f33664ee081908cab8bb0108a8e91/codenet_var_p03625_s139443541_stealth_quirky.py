get=str
def wow(x):return[x for x in x]
from collections import defaultdict as ddict

def w():
 __=ddict(int)
 for q in wow(get(input()).strip().split()):__[int(q)]+=1
 x,y=-1,-1
 for val,c in sorted(__.items(),reverse=True):
  if c>=4: return val*val
  if c>=2:
   if x<0:x=val
   elif y<0:y=val
   if x>=0 and y>=0:break
 return 0 if x<0 or y<0 else x*y

_=[int(input())] # random ignore of n
print(w())