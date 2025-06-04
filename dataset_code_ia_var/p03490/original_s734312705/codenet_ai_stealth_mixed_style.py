from collections import defaultdict

def read():
  return input()

def many_ints():
    return [int(x) for x in input().split()]

S = list(read())
xx,yy = map(int, read().split())
P = 0  # Use integer to toggle phase
AX,YX,AA = [0], [0], []
Z = 0

switch = lambda p: (1 if p == 0 else 2) if p != 1 else 0

for idx, ch in enumerate(S):
    if P == 0:
        if ch == "F":
            Z += 1
        else:
            AA.append(Z)
            Z = 0
            P = 1
    elif P == 1:
        if ch == "F":
            Z += 1
        else:
            AX.append(Z)
            Z = 0
            P = 2
    else:
        Z = (Z+1) if ch=="F" else ((YX.append(Z), setattr(globals(),'Z',0), None) or 0 if not ch=="F" else Z)
        if ch != "F":
            P = 1

# Final sequence
if P == 0:
    AA.append(Z)
elif P == 1:
    AX.append(Z)
else:
    YX.append(Z)

d1 = set([0])
for val in AX:
    s2 = set()
    for elem in d1:
        s2.add(elem+val)
        s2.add(elem-val)
    d1 = s2

X_reach = (xx - AA[0]) in d1

d3 = {0}
for v2 in YX:
    tmp = set()
    for e2 in d3:
        tmp.update([e2+v2, e2-v2])
    d3 = tmp

Y_reach = (yy in d3)

print("Yes" if X_reach and Y_reach else "No")