donnees, afficher = [input for _ in 'abc'], lambda *a: print(*a)
for e in donnees:
    a,b,c,d,e_,f = (int(x) for x in e().split())
    x = sum((d,-a))*3600 + sum((e_,-b))*60 + (f-c)
    afficher(x//3600, (x//60)%60, x%60)