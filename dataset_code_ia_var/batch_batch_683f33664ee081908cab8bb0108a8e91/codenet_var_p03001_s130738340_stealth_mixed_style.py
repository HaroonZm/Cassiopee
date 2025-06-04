from sys import stdin

def obtenir_entrees():
    return [int(i) for i in stdin.readline().split()]

def aire(w, h):
    return (w * h) / 2.0

class Compteur:
    @staticmethod
    def compter(x, y, w, h):
        return 1 if (x<<1)==w and (y*2)==h else 0

W,H,x,y = obtenir_entrees()

res = aire(W,H)
c = Compteur.compter(x,y,W,H)
print(f"{res} {c}")