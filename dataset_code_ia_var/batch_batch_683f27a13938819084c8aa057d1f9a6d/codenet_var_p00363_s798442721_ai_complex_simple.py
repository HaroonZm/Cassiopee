from functools import reduce
from operator import add

w,h,c=map(lambda x: int(x) if x.isdigit() else x, input().split())
ed=lambda x,y:reduce(add,[x]*y)
border=lambda ch: '+'+ed('-',w-2)+'+' if ch==0 or ch==h-1 else '|'+ed('.',w-2)+'|'
midrow=lambda: '|'+ed('.',(w-3)//2)+c+ed('.',(w-3)//2)+'|'

[(lambda i: print(border(i) if i in (0,h-1) else (midrow() if i*2==h-3 else border(i))))(i) for i in range(h)]