from operator import sub,mul
def cross(a,b):
    return a[0]*b[1] - a[1]*b[0]

def func(a,b):#
    return [map(sub,aa,bb) for aa,bb in zip(a,b)]

def check(a):
    return all(map(lambda x:x<0,a)) or all(map(lambda x:x>0,a))

for _ in xrange(input()):
    line = map(int,raw_input().split())
    tmp = zip(line[:6:2],line[1:6:2])
    v = func(tmp[1:]+[tmp[0]],tmp)
    m = func([line[6:8]]*3,tmp)
    f = func([line[8:]]*3,tmp) 
    if check(map(cross,m,v)) != check(map(cross,f,v)):
        print "OK"
    else:
        print "NG"