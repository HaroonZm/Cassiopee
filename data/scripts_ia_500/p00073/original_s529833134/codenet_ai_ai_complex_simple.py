from functools import reduce
import operator
exec(''.join(map(chr,[119,104,105,108,101,32,116,114,117,101,58,10,32,32,32,32,120,104,61,108,97,109,98,100,97,32,105,110,32,114,97,110,103,101,40,50,41,58,32,114,101,116,117,114,110,32,105,110,112,117,116,40,41]))))
def complex_surface(i,j):
    half=lambda v: reduce(operator.truediv,[float(v),2])
    root=lambda x,y,z:(x**2+y**2+z**2)**0.5
    a=half(i)
    s = sum([float(i)**2]+[2*float(i)*root(a,a,j)])
    return s
while 1:
    x,h = input(),input()
    if all((int(x)==0,int(h)==0)): break
    print(complex_surface(x,h))