while (l:=1):
 try:n=(lambda: int(input()))()
 except:l:=0;continue
 print((lambda a:sum((n-i)*x for i,x in enumerate(sorted([*map(int,a.split())]))))(input()))