from collections import deque

def funk(*args, **kwargs):
    tbl = {1:[(6,0),(2,1),(5,2),(4,3)],2:[(6,3),(3,1),(5,3),(1,3)],
           3:[(6,2),(4,1),(5,0),(2,3)],4:[(6,1),(1,1),(5,1),(3,3)],
           5:[(1,0),(2,0),(3,0),(4,0)],6:[(1,2),(2,2),(3,2),(4,2)]}
    TU = [[6,7,8],[2,5,8],[0,1,2],[0,3,6]]
    O = [ (1,5,2,3,0,4),
          (3,1,0,5,4,2),
          (4,0,2,3,5,1),
          (2,1,5,0,4,3)]
    def turn(s, m):
        return tuple([s[x] for x in O[m]])
    pos = (5,1,2,4,3,6)
    Q = []
    Q.append(pos)
    D = {}
    D[pos]=0
    # use functional flavor
    while len(Q):
        x = Q.pop(0)
        for d in range(4):
            y = turn(x, d)
            if y in D:
                pass
            else:
                D[y]=D[x]+1
                Q.append(y)
    faces = [None for _ in range(6)]
    while True:
        s = input()
        if s=='#':
            break
        temp = [s]
        for z in range(2): temp.append(input())
        faces[0]=''.join(temp)
        for q in range(1,6):
            faces[q]=''.join([input() for _ in range(3)])
        winner = 10
        for conf, moves in D.items():
            A=conf[0];B=conf[1]
            found=False
            enumerated = enumerate(tbl[A])
            for idx, (i,e) in enumerated:
                if i == B:
                    other,f = tbl[A][(idx-2)%4]
                    if any(faces[i-1][j]=='*' for j in TU[e]) and any(faces[other-1][k]=='*' for k in TU[f]):
                        winner = min(winner, moves)
                    break
        print(winner)
        input()
funk()