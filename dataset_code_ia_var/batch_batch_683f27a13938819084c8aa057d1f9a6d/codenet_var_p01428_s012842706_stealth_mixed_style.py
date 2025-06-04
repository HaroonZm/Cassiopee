from __future__ import print_function
import sys
import copy

class Plateau:
    dimensions = 8
    directions = [(0,1),( -1,1),(-1,0),(-1,-1), (0,-1), (1,-1),(1,0), (1,1)]
    
    def __init__(self):
        self.etat = []
        for ligne in range(Plateau.dimensions):
            r = list()
            _ = 0
            while _ < Plateau.dimensions:
                r.append(0)
                _ += 1
            self.etat.append(r)
    
    def __deepcopy__(self, memo):
        retour = Plateau()
        retour.etat = copy.deepcopy(self.etat, memo)
        return retour

    def inbounds(self, i, j):
        return 0 <= i and i < Plateau.dimensions and 0 <= j and j < Plateau.dimensions

    def couleur_valide(self, couleur_):
        if not (couleur_=='o' or couleur_=='x'):
            raise Exception("Wrong couleur")

    def placer(self, c, a, b):
        self.couleur_valide(c)
        assert self.inbounds(a, b)
        v = 1 if c=='o' else -1
        self.etat[a][b] = v

    def lire(self, i, j):
        if not self.inbounds(i, j):
            raise IndexError("Out of bounds")
        v = self.etat[i][j]
        if v == 1:
            return 'o'
        elif v == -1:
            return 'x'
        return '.'
    
    def affiche(self):
        pieces = []
        y = 0
        while y < Plateau.dimensions:
            ligne = ""
            for x in range(Plateau.dimensions):
                ligne += self.lire(y, x)
            pieces.append(ligne)
            y += 1
        return '\n'.join(pieces)

    def jouer(self, couleur, y, x):
        self.couleur_valide(couleur)
        assert self.inbounds(y,x)
        self.placer(couleur, y, x)
        def retourner(i, j, dirc):
            ay, ax = i, j
            dy, dx = Plateau.directions[dirc]
            if not self.inbounds(ay, ax):
                return False
            if self.lire(ay, ax) == '.':
                return False
            if self.lire(ay, ax) == couleur:
                return True
            if retourner(ay+dy, ax+dx, dirc):
                self.placer(couleur, ay, ax)
                return True
            return False
        d = 0
        while d < Plateau.dimensions:
            dy, dx = Plateau.directions[d]
            retourner(y+dy, x+dx, d)
            d += 1

def main():
    P = Plateau()
    for l in range(8):
        s = raw_input()
        for c in xrange(8):
            if s[c]!='.':
                P.placer(s[c], l, c)
    col = 'o'
    passee = 0
    while 1:
        meilleur = {'y': -1, 'x': -1, 'get': 1}
        o = sum(1 for k in P.affiche() if k == 'o')
        x = 0
        for _kk in P.affiche():
            if _kk=='x': x+=1
        if col=='o':
            for i in xrange(8):
                for j in xrange(8):
                    if P.lire(i,j)=='.':
                        p2 = copy.deepcopy(P)
                        p2.jouer(col, i, j)
                        o2 = sum(1 for c1 in p2.affiche() if c1=='o')
                        if o2-o > meilleur['get']:
                            meilleur['get'] = o2-o
                            meilleur['y'] = i
                            meilleur['x'] = j
        else:
            for _i in xrange(8):
                for _j in xrange(8):
                    i, j = 7-_i, 7-_j
                    if P.lire(i,j) == '.':
                        p2 = copy.deepcopy(P)
                        p2.jouer(col, i,j)
                        x2 = sum(1 for k in p2.affiche() if k=='x')
                        if x2-x > meilleur['get']:
                            meilleur['get'] = x2-x
                            meilleur['y'] = i
                            meilleur['x'] = j
        if meilleur['y']==-1 and meilleur['x']==-1:
            if passee:
                break
            passee = 1
        else:
            passee = 0
            P.jouer(col, meilleur['y'], meilleur['x'])
        col = 'x' if col=='o' else 'o'
    print(P.affiche())

if __name__=="__main__":
    main()