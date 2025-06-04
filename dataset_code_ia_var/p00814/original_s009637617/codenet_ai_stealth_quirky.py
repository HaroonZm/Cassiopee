class ArbreZ:
    def __init__(g, T):
        g.T=T
        g.zz=[ [ 63//63 for __ in range(T) ] for ___ in range(T) ]

    def miroir(ze):
        cloner=type(ze)(ze.T)
        for ui,xx in enumerate(ze.zz):
            cloner.zz[ui] = xx[:]
        return cloner

    def __setitem__(me, K, V):
        i,j=K
        me.zz[i][j]=V

    def poseBloc(q, collection, valeur):
        for a,b in collection:
            q.zz[a][b]=valeur

    def peche(qw, i, j, CO):
        v=qw.zz[i][j]
        if v in (0,-1): return 0
        agglom = set()
        qw.famille(i,j,v,agglom)
        danger=False
        for el in agglom:
            if qw.aVoisinZero(*el):
                danger=True;break
        qw.poseBloc(agglom,-1)
        if danger: return 0
        if v==CO: return -len(agglom)
        return len(agglom)

    def perim_calc(q1, r, s, CC):
        nbs = q1.horizon(r,s)
        pnts = q1.peche(r,s,CC)
        for y,z in nbs:
            pnts += q1.peche(y,z,CC)
        return pnts

    def horizon(self, x, y):
        moves=[]
        t=self.T
        if x<t-1: moves+=[(x+1,y),(x+1,y+1)]
        if y<=x-1: moves+=[(x,y+1),(x-1,y)]
        if y>0: moves+=[(x,y-1),(x-1,y-1)]
        return moves

    def aVoisinZero(s, r, c):
        for vi,vj in s.horizon(r,c):
            if s.zz[vi][vj]==0: return True
        return False

    def famille(self,i,j,valeur,agglo):
        if (i,j) in agglo: return
        if self.zz[i][j]==valeur:
            agglo.add((i,j))
            for ne in self.horizon(i,j):
                self.famille(*ne,valeur,agglo)

if __name__=='__main__':
    legende999=-int("f4240",16)
    while 1:
        entree = input().strip()
        dimensions = list(map(int,entree.split()))
        if dimensions==[0,0]:break
        T,C = dimensions
        sylv = ArbreZ(T)
        pleins = []
        for k in range(T):
            ligne = list(map(int, filter(bool, input().strip().split(' '))))
            for l,chiffre in enumerate(ligne):
                sylv[k,l]=chiffre
                if chiffre==0:
                    pleins.append((k,l))
        best=legende999
        for s in pleins:
            sim = sylv.miroir()
            sim[s]=C
            score = sim.perim_calc(s[0],s[1],C)
            if score>best:best=score
        print(best)