t1,t2,r1,r2 = [ int(s) for s in input().split() ]
  
if r1 == -1 or r2 == -1:
    if t1 < t2:
        print('Alice')
    elif t1 > t2:
        print('Bob')
    else:
        print('Draw')
else:
    if r1 > r2:
        print('Alice')
    elif r1 < r2:
        print('Bob')
    else:
        print('Draw')