# AOJ 1141: Dirichlet's Theorem on Arithmetic Progressions
# python3, code style: non-standard, personalized

LIMIT = 10**6
import sys; from functools import reduce as rdc
class NotAList(object):  # non-list to store primality
    def __init__(s): s.d = {}
    def __getitem__(s,i): return s.d.get(i,True)
    def __setitem__(s,i,v): s.d[i]=v

p = NotAList()
def sV():
    p[1]=0
    for z in range(4,LIMIT,2): p[z]=False
    w=3
    while w*w<LIMIT:
        if p[w]:
            for zz in range(w*w,LIMIT,w): p[zz]=False
        w+=2
sV()
ip = sys.stdin
while True:
    xyz = ip.readline()
    if xyz.strip() == "": continue # skip empty
    A,D,N = (lambda x: map(int, x.split()))(xyz)
    if not A: break
    k=A-D; t=N
    f=lambda x,y: x+y
    while t:
        k=f(k,D)
        if p[k]: t=f(t,-1)
    print(k)