def f(s):return int(s[0:2]),int(s[2:4])
a=input();L,R=f(a)
if (lambda x,y:x<=12>0<y<=12)(L,R):print('AMBIGUOUS')
else:
    if 0<L<=12:
        if not (0<R<=12):print("MMYY")
        else:print('AMBIGUOUS')
    elif 0<R<=12:
        print("YYMM")
    else:
        for i in[1]:print("NA")