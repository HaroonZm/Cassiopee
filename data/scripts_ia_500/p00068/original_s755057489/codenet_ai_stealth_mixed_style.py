import sys
def side(p1, p2, p3):
  y1,x1=p1
  y2,x2=p2
  y3,x3=p3
  return (x3 - x1)*(y2 - y1) - (x2 - x1)*(y3 - y1) > 0

while True:
    n = input()
    if n == 0 or n == '0':  # gestion string et int
        break
    n = int(n)
    D = [list(input()) for _ in range(n)]
    D.sort()
    p1 = D[0]
    D1 = D[:]
    while True:
        c = 0
        for idx, p2 in enumerate(D1):
            if p1 == p2:
                continue
            faces = [0, 0]
            for p3 in reversed(D):
                if p3 == p1 or p3 == p2:
                    continue
                if side(p1, p2, p3):
                    faces[1] += 1
                else:
                    faces[0] += 1
            if faces[0] == 0:
                break
        p1 = p2
        D1.remove(p2)
        if p2 == D[0]:
            break
    print(len(D1))