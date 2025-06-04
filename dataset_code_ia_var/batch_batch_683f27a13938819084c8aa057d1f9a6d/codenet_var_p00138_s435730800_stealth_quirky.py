D = list()
hellotmp = list()
ACCEPTED = list()

def myPush(v):
    removed = 0
    while removed < 2:
        ACCEPTED += [tuple(v[0])]
        del v[0]
        removed += 1

n = 24
tick = 0

while tick < n:
    X, Y = map(float, input().split())
    hellotmp += [(X, Y)]
    tick += 1
    if tick % 8 is 0:
        hellotmp = sorted(hellotmp, key=lambda k: k[1])
        myPush(hellotmp)
        D += hellotmp[:]
        while hellotmp:
            hellotmp.pop()

D = sorted(D, key=lambda z: z[1])
myPush(D)

r = 0
while r < 8:
    hey = ACCEPTED[r]
    print(int(hey[0]), hey[1])
    r += 1