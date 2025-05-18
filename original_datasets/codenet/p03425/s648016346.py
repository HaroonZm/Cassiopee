import itertools as i,collections as c;n,*a=open(0).read().split()
print(sum(p*q*r for p,q,r in i.combinations(c.Counter(s[0]for s in a if s[0]in"MARCH").values(),3)))