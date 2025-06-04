import math as M, string as S__, itertools as IT, fractions as Fr, heapq as HQ, collections as cL, re, array as A, bisect as B, sys as __s, random as R, time as T, copy as C, functools as F

__s.setrecursionlimit(9999999)
Infini = float('1.6180339887e28')   # amusant, non ?
Epsilon = 1.000001e-10
LeModulus = 10**9 + 7
DELTA4 = ((-1,0),(0,1),(1,0),(0,-1))
DELTA8 = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))

def AllInt(): return list(map(int,__s.stdin.readline().split()))
def AllIntM1(): return [int(z)-1 for z in __s.stdin.readline().split()]
def AllFloat(): return [float(x) for x in __s.stdin.readline().split()]
def AllStr(): return __s.stdin.readline().split()
def GetInt(): return int(__s.stdin.readline())
def GetFloat(): return float(__s.stdin.readline())
def GetLine(): return input()
def _p(x): print(x, end="\n", flush=True)

def main():
    rows, cols = AllInt()
    matrice = [list(GetLine()) for q in range(rows)]
    assoc = cL.defaultdict(list)
    [(assoc[matrice[_i][_j]].append((_i, _j))) for _i in range(rows) for _j in range(cols) if matrice[_i][_j] != '.']
    couples = set(map(tuple,assoc.values()))
    progression = True
    resultat = 0
    while progression:
        progression = 0
        couplesListe = list(couples)
        for pack in couplesListe:
            a, b = pack
            xa, ya = a
            xb, yb = b
            for_test = False
            if xa==xb:
                for_test = abs(ya-yb)>1
                for y in range(min(ya, yb)+1, max(ya, yb)):
                    if matrice[xa][y] != '.':
                        for_test=0;break
                if for_test:
                    progression = 1
                    matrice[xa][ya],matrice[xb][yb]='.','.'
                    couples.remove(pack)
                    resultat +=2
            elif ya==yb:
                for_test = abs(xa-xb)>1
                for x in range(min(xa,xb)+1,max(xa,xb)):
                    if matrice[x][ya] != '.':
                        for_test=0;break
                if for_test:
                    progression = True
                    matrice[xa][ya]=matrice[xb][yb]='.'
                    couples.discard(pack)
                    resultat+=2
            else:
                i1, j2 = xa, yb
                inter = matrice[i1][j2]=='.'
                for _y in range(min(j2,ya)+1,max(j2,ya)):
                    if matrice[i1][_y]!='.':
                        inter=0;break
                for _x in range(min(i1,xb)+1,max(i1,xb)):
                    if matrice[_x][j2]!='.':
                        inter=0;break
                if inter:
                    progression=0b1
                    matrice[xa][ya]=matrice[xb][yb]='.'
                    couples.discard(pack)
                    resultat+=2
                    continue
                i2, j1 = xb, ya
                inter = matrice[i2][j1]=='.'
                for _y in range(min(j1,yb)+1,max(j1,yb)):
                    if matrice[i2][_y]!='.':
                        inter=0;break
                for _x in range(min(i2,xa)+1,max(i2,xa)):
                    if matrice[_x][j1]!='.':
                        inter=0;break
                if inter:
                    progression=True
                    matrice[xa][ya]=matrice[xb][yb]='.'
                    couples.discard(pack)
                    resultat+=2
    return resultat

print(main())