d__=dict()
[ (lambda k,v: d__.update({k:d__.get(k,0)+int(v)}))(*input().split()) for _ in range(int(input())) ]
def wtf(x):
 r=0
 for i,c in enumerate(x[::-1]):
  r+=27**i*(ord(c)-64)
 return r,x
for key in sorted(d__.keys(),key=wtf):
 print(key,d__[key])