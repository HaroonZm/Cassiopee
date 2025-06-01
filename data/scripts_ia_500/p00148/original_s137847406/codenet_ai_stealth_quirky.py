L=list((39,)+tuple(range(1,39)))
from sys import stdin
for c in iter(stdin.read, ''):
 try:print(f'3C{L[int(c)%39]:02d}')
 except:break