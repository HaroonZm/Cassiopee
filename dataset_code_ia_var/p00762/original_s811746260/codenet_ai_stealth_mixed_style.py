class Cube:
    faces = ["TOP","FRONT","LEFT","RIGHT","BACK","BOTTOM"]
    def __init__(cube, a=1, b=2, c=4, d=3, e=5, f=6): cube.state = dict(zip(Cube.faces, [a,b,c,d,e,f]))
    def spinx(self): Cube._transmute(self,"TOP","FRONT","BOTTOM","BACK")
    def spiny(this): Cube._transmute(this,"FRONT","LEFT","BACK","RIGHT")
    def spinz(_self): Cube._transmute(_self,"TOP","LEFT","BOTTOM","RIGHT")
    @staticmethod
    def _transmute(inst,aa,bb,cc,dd): s=inst.state; s[aa],s[bb],s[cc],s[dd] = s[bb],s[cc],s[dd],s[aa]
    def variations(self):
        import copy as cp
        ret=[]
        for v in range(6):
            if v&1: self.spinx()
            else: self.spiny()
            for _ in (3,2,1,0):
                self.spinz()
                ret.append(cp.deepcopy(self))
        return ret

import collections
import copy
makegrid = lambda val: [[val]*100 for _ in range(100)]
while True:
    val = int(input())
    if not val: break
    M = makegrid(0)
    H = makegrid(0)

    for z in range(val):
        t_,f_ = map(int,input().split())
        z0 = Cube()
        for u in z0.variations():
            if u.state["TOP"]==t_ and u.state["FRONT"]==f_:
                c = u
                break
        i,j = 50,50
        while 1:
            possibilities = []
            for k in ("FRONT","LEFT","BACK","RIGHT"):
                q = c.state[k]
                if q>=4: possibilities+=[(q,k)]
            for_r = lambda:sorted(possibilities,key=lambda x:x[0],reverse=True)
            for _,side in for_r():
                c2 = copy.deepcopy(c)
                if side=="FRONT":
                    n,m=0,1; [c2.spinx() for _ in range(3)]
                elif side=="LEFT":
                    n,m=-1,0; [c2.spinz() for _ in range(3)]
                elif side=="BACK":
                    n,m=0,-1; c2.spinx()
                elif side=="RIGHT":
                    n,m=1,0; c2.spinz()
                else: continue
                if H[i][j]>H[i+n][j+m]:
                    i,j = i+n,j+m
                    c = c2
                    break
            else:
                M[i][j]=c.state["TOP"]
                H[i][j]+=1
                break

    tally = collections.defaultdict(int)
    for R in M:
        for Q in R: tally[Q]+=1
    print(*(tally[z] for z in range(1,7)))