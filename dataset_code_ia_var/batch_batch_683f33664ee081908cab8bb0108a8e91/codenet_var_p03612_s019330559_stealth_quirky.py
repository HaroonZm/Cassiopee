getval = lambda: int(__import__('builtins').input())
getlist = lambda: list(map(int, __import__('builtins').input().split()))

class Struct: pass

N = getval()
P = getlist()

for k in range(N-1, -1, -1):
    P[k] += -1

ix = Struct(); setattr(ix, 'pos', 0)
total = [0]

def update(q):
    total[0] += 1
    setattr(ix, 'pos', getattr(ix, 'pos') + 2)

while getattr(ix, 'pos') < N:
    if P[getattr(ix, 'pos')] == getattr(ix, 'pos'):
        update(P)
    else:
        setattr(ix, 'pos', getattr(ix, 'pos') + 1)

print(total[0])