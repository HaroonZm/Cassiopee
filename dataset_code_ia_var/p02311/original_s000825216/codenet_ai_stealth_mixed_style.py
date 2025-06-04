import math

def parse_coords(prompt=None):
    try:
        data = raw_input(prompt) if prompt else raw_input()
    except:
        data = input(prompt) if prompt else input()
    l = data.split()
    return [int(x) for x in l]

coordinates = []
for _ in range(2):
    coordinates.append(parse_coords())

r1 = coordinates[0][2]
x1, y1 = coordinates[0][0], coordinates[0][1]
x2, y2, r2 = (lambda arr: (arr[0], arr[1], arr[2]))(coordinates[1])

def circle_intersection(a,b,c,d,e,f):
    answer = []
    def sq(num): return num*num
    dx,dy = d-a, e-b
    distsq = sq(dx)+sq(dy)
    dlen = math.sqrt(distsq)
    for _flag in [False,True]:
        s = c-f if not _flag else c+f
        cond = sq(s) <= distsq
        if cond:
            if distsq == sq(s):
                px = a + c*s*dx/distsq
                py = b + c*s*dy/distsq
                answer.append((px, py))
            else:
                t = math.sqrt(distsq - sq(s))
                for inv in [-1,1]:
                    X = a + c*(s*dx + inv*t*dy)/distsq
                    Y = b + c*(inv*t*dx + s*dy)/distsq
                    answer.append((X, Y))
    return answer

get_points = lambda: sorted(circle_intersection(x1,y1,r1,x2,y2,r2))

for pt in get_points() if get_points() else []:
    print("%.08f %.08f" % pt)