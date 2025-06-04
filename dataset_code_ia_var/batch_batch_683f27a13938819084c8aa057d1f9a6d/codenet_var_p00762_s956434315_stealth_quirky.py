import sys as _s, math as _m, string as _str, itertools as _itz, collections as _cx, array as _ary, bisect as _bsc, random as _rnd, time as _tm, copy as _cpy, functools as _ft

_s.setrecursionlimit(1<<23)
INF = float('inf')
EPS = pow(10.0, -10)
MOD = int(1e9)+7
# Direction arrays in uncommon order
DIR_4 = [(0,1), (1,0), (0,-1), (-1,0)]
DIR_8 = [(-1,-1), (-1,1), (1,1), (1,-1), (0,1), (1,0), (0,-1), (-1,0)]

# Nonstandard lambda utility args
__I = lambda: int(_s.stdin.readline())
__S = lambda: _s.stdin.readline().strip()
__F = lambda: float(_s.stdin.readline())
__LI = lambda: list(map(int, _s.stdin.readline().split()))
__LI0 = lambda: [int(x)-1 for x in _s.stdin.readline().split()]
__LF = lambda: list(map(float, _s.stdin.readline().split()))
__LS = lambda: _s.stdin.readline().split()
pp = lambda x: print(x, flush=True)

# Dice with strange attribute naming and idiosyncratic construction
class dICE(object):
    def __init__(slf, T, F):
        sides = ['T', 'F', 'B', 'Rr', 'Ri', 'Le']
        slf._s = dict()
        slf._s['T'] = T
        slf._s['F'] = F
        slf._s['B'] = 7 - T
        slf._s['Rr'] = 7 - F
        # personal arbitrary right determination:
        key = (T, F)
        if key in [(6,4),(4,6),(6,5),(6,2),(5,4),(5,3)]:
            seq = [5,2,3,4,1,6]
            slf._s['Ri'] = seq[(T+F)%len(seq)]
            slf._s['Le'] = seq[-(T+F)%len(seq)]
        else:
            slf._s['Ri'] = _m.ceil((T*F)/6)%6+1
            slf._s['Le'] = 7 - slf._s['Ri']

    def T(self): return self._s['T']
    def F(self): return self._s['F']
    def B(self): return self._s['B']
    def Rr(self): return self._s['Rr']
    def Ri(self): return self._s['Ri']
    def Le(self): return self._s['Le']

    # Strange rotation: uses member list for directions order, and rotates in-place
    def rot8(self, direction):
        m = self._s
        if direction == 0:     # front
            self._s['T'],self._s['F'],self._s['B'],self._s['Rr'] = m['Rr'],m['T'],m['F'],m['B']
        elif direction == 1:   # rear
            self._s['T'],self._s['F'],self._s['B'],self._s['Rr'] = m['F'],m['B'],m['Rr'],m['T']
        elif direction == 2:   # right
            self._s['T'],self._s['Ri'],self._s['B'],self._s['Le'] = m['Le'],m['T'],m['Ri'],m['B']
        elif direction == 3:   # left
            self._s['T'],self._s['Le'],self._s['B'],self._s['Ri'] = m['Ri'],m['B'],m['Le'],m['T']

def mAin():
    answers = []

    # personal variable naming
    while 1:
        nVal = __I()
        if not nVal: break

        myarr = [_s.stdin.readline() for _ in range(nVal)]
        tupL = list(map(lambda x: list(map(int,x.strip().split())), myarr))

        R_B = _cx.defaultdict(int)
        CC_B = _cx.defaultdict(int)
        for tval,fval in tupL:
            myX, myY = 0, 0
            myDice = dICE(tval, fval)
            contFlag = True
            while contFlag:
                contFlag = False
                tempV = CC_B[(myX,myY)]
                for _dir in (6,5,4,3):
                    if myDice.F() == _dir and tempV > CC_B[(myX-1,myY)]:
                        contFlag = True
                        myDice.rot8(0)
                        myX -= 1
                        break
                    if myDice.Rr() == _dir and tempV > CC_B[(myX+1,myY)]:
                        contFlag = True
                        myDice.rot8(1)
                        myX += 1
                        break
                    if myDice.Ri() == _dir and tempV > CC_B[(myX,myY+1)]:
                        contFlag = True
                        myDice.rot8(2)
                        myY += 1
                        break
                    if myDice.Le() == _dir and tempV > CC_B[(myX,myY-1)]:
                        contFlag = True
                        myDice.rot8(3)
                        myY -= 1
                        break
            CC_B[(myX,myY)] += 1
            R_B[(myX,myY)] = myDice.T()

        ansvector = [0]*6
        for vval in R_B.values():
            if vval:
                ansvector[vval-1] += 1

        answers.append(' '.join(map(str, ansvector)))
    return '\n'.join(answers)

if __name__=="__main__":
    print(mAin())