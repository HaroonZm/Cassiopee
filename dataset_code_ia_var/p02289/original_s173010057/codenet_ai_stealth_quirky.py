import heapq as h ; S = __import__('sys').stdin.readline
X=[] ; O=print ; _=h.heappush ; __=h.heappop
while 1:
 I=S()
 if I[:2]=='en': quit()
 elif I[0]=='e':
  O(-__(X))
 else:
  _,v=I.split(); _(X,-int(v))