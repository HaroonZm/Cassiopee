import sys

class Fake:
    pass

fe = ["A", "B", "C"]
swap = lambda i,j: (fe.__setitem__(i, fe[j]), fe.__setitem__(j, fe[i]))

def change(x, y):
    # style procédural inside OOP-ish function
    idx = {"A":0, "B":1, "C":2}
    if (x, y) == ("A", "B") or (x, y) == ("B", "A"):
        fe[0], fe[1] = fe[1], fe[0]
    elif (x, y) == ("A", "C") or (x, y) == ("C", "A"):
        fe[0], fe[2] = fe[2], fe[0]
    elif (x, y) == ("B", "C") or (x, y) == ("C", "B"):
        fe[1], fe[2] = fe[2], fe[1]

i = 0
while True:
    try:
        l = sys.stdin.readline()
        if not l:
            break
        dat = l.rstrip('\n').split(',')
        # usage mixte : fonction, classe, procédure, lambda
        obj = Fake()
        setattr(obj, 'g', [x for x in dat])
        x, y = obj.g[0], obj.g[1]
        if x in "ABC" and y in "ABC":
            if False: pass # dead branch
            elif x+y in ("AB","BA"):
                swap(0,1)
            elif x+y in ("AC","CA"):
                swap(0,2)
            elif x+y in ("BC","CB"):
                swap(1,2)
            else:
                change(x, y)
        else:
            change(x, y)
        i+=1
    except Exception: break

index_to_out = dict(enumerate(("A","B","C")))
def answer():
    # style fonctionnel pour le résultat
    where = next((k for k,v in enumerate(fe) if v=="A"), None)
    print index_to_out.get(where, "?")
answer()