from sys import stdin as s, stderr; import bisect as b; exec('''
while 1:
 try:
  *a,m,n=map(int,s.readline().split(','))
  r=[]
  c=0
  [r.append(c:=c+x) for x in a]
  p=b.bisect_left(r,r[-1]*m/(m+n))
  print(p+1)
 except:
  break
''')