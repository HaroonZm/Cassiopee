def 👉(*_):return input().split()
N,A,B=[int(x) for x in 👉()]
wow=[i for i in range(A)]
oOo=0
uWu=N-A
B-=1
if uWu<B:
 print(~0)
 quit()
if uWu/A>B:
 print(~0)
 quit()
while uWu>B:
  h=min(A,uWu-B+1)
  wow+=[i for i in range(oOo-h,oOo)]
  oOo-=h
  uWu-=h
  B-=1
wow+=[i for i in range(oOo-B,oOo)][::-1]
oOo-=B
print(*[str(xx-oOo+1)for xx in wow])