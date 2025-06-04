import sys
import math
import random

def dist(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)

def ball_two(a,b):
    center = [(a[0]+b[0])/2,(a[1]+b[1])/2,(a[2]+b[2])/2]
    radius = dist(a,b)/2
    return center,radius

def ball_three(a,b,c):
    A = [b[i]-a[i] for i in range(3)]
    B = [c[i]-a[i] for i in range(3)]

    cross = [A[1]*B[2]-A[2]*B[1],
             A[2]*B[0]-A[0]*B[2],
             A[0]*B[1]-A[1]*B[0]]
    denom = 2*sum(x*x for x in cross)
    if abs(denom)<1e-15:
        # Points are colinear, return the biggest segment's ball_two
        dists = [(dist(a,b), (a,b)),(dist(a,c),(a,c)),(dist(b,c),(b,c))]
        dmax,pair = max(dists,key=lambda x:x[0])
        return ball_two(*pair)
    A2 = sum(x*x for x in A)
    B2 = sum(x*x for x in B)
    crosA = [A[1]*cross[2]-A[2]*cross[1],
             A[2]*cross[0]-A[0]*cross[2],
             A[0]*cross[1]-A[1]*cross[0]]
    crosB = [B[1]*cross[2]-B[2]*cross[1],
             B[2]*cross[0]-B[0]*cross[2],
             B[0]*cross[1]-B[1]*cross[0]]
    alpha = B2*(sum(crosA[i]*cross[i] for i in range(3)))/denom
    beta = A2*(sum(crosB[i]*cross[i] for i in range(3)))/denom
    center = [a[i]+(alpha*A[i]+beta*B[i])/(2) for i in range(3)]
    radius = dist(center,a)
    return center,radius

def ball_four(a,b,c,d):
    # Solve linear system to find sphere through 4 points
    def mat_vec_mul(m,v):
        return [sum(m[i][j]*v[j] for j in range(3)) for i in range(3)]
    A = []
    B = []
    for p in [a,b,c,d]:
        A.append([2*p[0],2*p[1],2*p[2]])
        B.append(p[0]*p[0]+p[1]*p[1]+p[2]*p[2])
    M = [ [A[i][j]-A[0][j] for j in range(3)] for i in range(1,4)]
    Y = [B[i]-B[0] for i in range(1,4)]
    # Solve Mx=Y
    det = (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
          -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
          +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
    if abs(det)<1e-15:
        # Points are coplanar or degenerate, return max ball_two
        pts = [a,b,c,d]
        dists = [(dist(p1,p2),(p1,p2)) for i,p1 in enumerate(pts) for p2 in pts[i+1:]]
        dmax,pair = max(dists,key=lambda x:x[0])
        return ball_two(*pair)
    def det3(m):
        return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
             - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
             + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
    Mx = [[Y[0],M[0][1],M[0][2]],
          [Y[1],M[1][1],M[1][2]],
          [Y[2],M[2][1],M[2][2]]]
    My = [[M[0][0],Y[0],M[0][2]],
          [M[1][0],Y[1],M[1][2]],
          [M[2][0],Y[2],M[2][2]]]
    Mz = [[M[0][0],M[0][1],Y[0]],
          [M[1][0],M[1][1],Y[1]],
          [M[2][0],M[2][1],Y[2]]]
    x = det3(Mx)/det
    y = det3(My)/det
    z = det3(Mz)/det
    center = [x,y,z]
    radius = dist(center,a)
    return center,radius

def is_in_sphere(p,c,r):
    return dist(p,c)<=r+1e-12

def trivial_ball(points):
    if not points:
        return ([0.0,0.0,0.0],0.0)
    if len(points)==1:
        return (points[0],0.0)
    if len(points)==2:
        return ball_two(points[0],points[1])
    if len(points)==3:
        return ball_three(points[0],points[1],points[2])
    return ball_four(points[0],points[1],points[2],points[3])

def welzl(P,R,n):
    if n==0 or len(R)==4:
        return trivial_ball(R)
    p = P[n-1]
    c,r = welzl(P,R,n-1)
    if is_in_sphere(p,c,r):
        return c,r
    else:
        return welzl(P,R+[p],n-1)

def min_enclosing_sphere(points):
    P = points[:]
    random.shuffle(P)
    c,r = welzl(P,[],len(P))
    return r

input_lines = sys.stdin.read().strip().split('\n')
i=0
while True:
    if i>=len(input_lines): break
    n = int(input_lines[i])
    i+=1
    if n==0:
        break
    pts = []
    for _ in range(n):
        x,y,z = map(float,input_lines[i].split())
        i+=1
        pts.append([x,y,z])
    r = min_enclosing_sphere(pts)
    print(f"{r:.5f}")