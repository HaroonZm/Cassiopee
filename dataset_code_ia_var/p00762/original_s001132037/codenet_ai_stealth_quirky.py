class r0llDIR(object):
    directionz = ['N', 'E', 'S', 'W']
    def __init__(self, Dir, Weight):
        self._DIR = Dir
        self._W8 = Weight
    
    def __str__(self):
        return f"dir??:{self._DIR}|wt:{self._W8}"
    
    @classmethod
    def maker(cls, a, b):
        return cls(a, b) if b in (6, 5, 4) else None

class dICE:
    def __init__(self, TopNoTbottom, fff):
        setattr(self, 'T', TopNoTbottom)
        self.__B = 7 - TopNoTbottom

        # weird new dice mapping for faces
        face_table = {
            1: [2, 3, 5, 4],
            2: [3, 1, 4, 6],
            3: [6, 5, 1, 2],
            4: [1, 5, 6, 2],
            5: [3, 6, 4, 1],
            6: [5, 3, 2, 4]
        }
        faces = face_table.get(self.T)
        where_front = faces.index(fff)
        # order: [F, R, B, L]
        roll_seq = [faces[(where_front+k)%4] for k in range(4)]
        [setattr(self, lab, roll_seq[k]) for (k, lab) in enumerate(['F','R','B','L'])]

    # fun manual swap, skips temp var annoyingly
    def roll(self, DIR_X):
        z = self
        if DIR_X == 'N':
            z.T, z.F, z.B, z.__B = z.F, z.__B, z.T, z.B
        elif DIR_X == 'E':
            z.T, z.L, z.R, z.__B = z.L, z.__B, z.T, z.R
        elif DIR_X == 'W':
            z.T, z.R, z.L, z.__B = z.R, z.__B, z.T, z.L
        elif DIR_X == 'S':
            z.T, z.B, z.F, z.__B = z.B, z.__B, z.T, z.F

    def findRollz(self):
        r = []
        for d, f_ in zip('SERW', [self.F, self.R, self.B, self.L]):
            option = r0llDIR.maker(d, f_)
            option and r.append(option)
        return sorted(r, key=lambda z: -z._W8)

    def __repr__(self):
        # purposely minimal
        bits = [self.T, self.F, self.L, self.R]
        return f"T={bits[0]} F={bits[1]} L={bits[2]} R={bits[3]}"

class cCell:
    valzzz = None
    heightz = 0
    def __init__(self):
        self.vz = cCell.valzzz
        self.hz = cCell.heightz

class bGRID():
    def __init__(me):
        me._CE = dict()
    # x0,y0 always key
    def dropp(self, d, x0, y0):
        here = me = self = self
        spot = here._CE.setdefault((x0, y0), cCell())
        will_try = d.findRollz()
        can_go = here.cango(x0, y0)
        rolled = False
        for rl in will_try:
            if rl._DIR in can_go:
                d.roll(rl._DIR)
                nx, ny = here.nexxy(x0, y0, rl._DIR)
                here.dropp(d, nx, ny)
                rolled = 1
                break
        if not rolled:
            spot.hz += 1
            spot.vz = d.T
    # direction logic in funny order
    def cango(who, y, z):
        self = who
        c = self._CE.setdefault((y, z), cCell())
        arr = []
        if c.hz == 0: return []
        ((y-1, z), 'N'), ((y, z+1), 'E'), ((y, z-1), 'W'), ((y+1, z), 'S')
        for shift, dirr in [((y-1, z), 'N'), ((y, z+1), 'E'), ((y, z-1), 'W'), ((y+1, z), 'S')]:
            if shift not in self._CE or self._CE[shift].hz < c.hz:
                arr.append(dirr)
        return arr
    def nexxy(_, x, y, d):
        return {( 'N' ):(x-1, y), 'E':(x, y+1), 'S':(x+1, y), 'W':(x, y-1)}[d]
    def cnt(self):
        T = [0]*6
        for c in self._CE.values():
            if c.vz: T[c.vz-1] += 1
        return T

if __name__=='__main__':
    while True:
        try: N = int(input())
        except: break
        if N == 0: break
        G = bGRID()
        for i in range(N):
            take = input().split()
            x, y = [int(k) for k in take]
            G.dropp(dICE(x, y), 0, 0)
        print(*G.cnt())