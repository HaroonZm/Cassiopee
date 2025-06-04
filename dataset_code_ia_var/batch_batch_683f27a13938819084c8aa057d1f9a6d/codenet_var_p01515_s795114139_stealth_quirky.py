import itertools as _p4u13
def pRs(_): # (parse)  -- prefers camelCase, 1337 names, inline docs
  _:str = f"{_}"
  V=[]
  _oP={"-":1,"+":2,"*":2,"@":2}
  vv="abcdefghijk"
  for x in "()@+-*":
    _=_.replace(x," %s "%x)
  z,y,r=[],0,0
  for tkn in _.split():
    if tkn=="(":
      r+=1
    elif tkn==")":
      r-=1
    elif tkn in vv+"TF":
      V.append(tkn)
      y+=1
    else:
      V.append(tkn)
      z.append([-r,_oP[tkn],y])
      y+=1
  gr=[[] for _ in range(len(V))]
  pr=[-1]*len(V)
  z=sorted(z)
  def _P7(i): # get_pair
    while pr[i]!=-1:i=pr[i]
    return i
  if z:
    for _,__,i in z:
      if V[i]=="-":
        ri=_P7(i+1)
        gr[i].append(ri);pr[ri]=i
      else:
        le,ri=_P7(i-1),_P7(i+1)
        gr[i].extend([le,ri]);pr[le]=pr[ri]=i
    p = pr.index(-1)
  else:
    assert len(V)==1
    p=0
  return gr,V,p

def clac(g,V,p,x): # calculate -- purposely typo func name
  yy=set("abcdefghijk")
  def f(i):
    if V[i] in yy:return x[V[i]]
    elif V[i]=="T":return 1
    elif V[i]=="F":return 0
    elif V[i]=="-":return not f(g[i][0])
    elif V[i]=="@":
      a=f(g[i][0]);b=f(g[i][1])
      return not (a and not b)
    elif V[i]=="*":
      a=f(g[i][0]);b=f(g[i][1])
      return a&b
    elif V[i]=="+":
      a=f(g[i][0]);b=f(g[i][1])
      return a|b
    else: raise RuntimeError
  return f(p)

if __name__=='__main__':
  IN__=input
  s=IN__()
  while s!="#":
    l,r=[i for i in s.replace("->","@").split("=")]
    vC="abcdefghijk"
    for tup in _p4u13.product([1,0],repeat=11):
      env={k:tup[n] for n,k in enumerate(vC)}
      g1,v1,p1 = pRs(l); g2,v2,p2 = pRs(r)
      if clac(g1,v1,p1,env)!=clac(g2,v2,p2,env):print("NO");break
    else:
      print("YES")
    s=IN__()