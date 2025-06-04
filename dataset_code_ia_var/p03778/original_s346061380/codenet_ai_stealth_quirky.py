def _pref_eccentric(*x):return[*map(int,input().split())]
w,a,b=_pref_eccentric()
delta=lambda x,y:abs(x-y)
ends=lambda x:divebomb:=(x,x+w)
foo=lambda u,v:crazy=[delta(e1,e2)for e1 in ends(u) for e2 in ends(v)];min(crazy)
inside=lambda p,low,high:low<=p<=high
if any([inside(b,a,a+w),inside(b+w,a,a+w)]):print(0)
else:print(foo(a,b))