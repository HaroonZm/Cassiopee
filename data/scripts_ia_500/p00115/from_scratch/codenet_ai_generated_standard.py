import sys
def vec_sub(a,b): return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def length(a): return (a[0]*a[0]+a[1]*a[1]+a[2]*a[2])**0.5
def same_side(p1,p2,a,b):
    cp1=cross(vec_sub(b,a),vec_sub(p1,a))
    cp2=cross(vec_sub(b,a),vec_sub(p2,a))
    return dot(cp1,cp2)>=-1e-12
def point_in_triangle(p,a,b,c):
    # check if p is inside triangle abc
    return same_side(p,a,b,c) and same_side(p,b,a,c) and same_side(p,c,a,b)
def point_in_plane_triangle(p,a,b,c):
    # check coplanar and inside
    ab=vec_sub(b,a)
    ac=vec_sub(c,a)
    ap=vec_sub(p,a)
    n=cross(ab,ac)
    if abs(dot(n,ap))>1e-12:
        return False
    return point_in_triangle(p,a,b,c)
def line_plane_intersection(p0,p1,a,b,c):
    ab=vec_sub(b,a)
    ac=vec_sub(c,a)
    n=cross(ab,ac)
    dir=vec_sub(p1,p0)
    denom=dot(n,dir)
    if abs(denom)<1e-15:
        # line parallel to plane
        return None
    t=dot(n,vec_sub(a,p0))/denom
    if t< -1e-15 or t>1+1e-15:
        return None
    return (p0[0]+dir[0]*t,p0[1]+dir[1]*t,p0[2]+dir[2]*t), t
def point_in_segment(p,p0,p1):
    # check if p in segment p0p1 (within tolerance)
    v0=vec_sub(p1,p0)
    v1=vec_sub(p,p0)
    if dot(v0,v1)<-1e-15: return False
    if dot(v0,v0)+1e-15 < dot(v1,v1): return False
    return True
uaz=tuple(map(int,input().split()))
enemy=tuple(map(int,input().split()))
v1=tuple(map(int,input().split()))
v2=tuple(map(int,input().split()))
v3=tuple(map(int,input().split()))
# enemy inside barrier?
if point_in_plane_triangle(enemy,v1,v2,v3):
    print("MISS")
    sys.exit()
# check if barrier visible from UAZ (non degenerate angle)
if not (point_in_triangle(v1,uaz,v2,v3) or point_in_triangle(v2,uaz,v1,v3) or point_in_triangle(v3,uaz,v1,v2)):
    # Barrier not 'seen' as triangle from UAZ (problem states only such barriers affect)
    print("HIT")
    sys.exit()
# check intersection of beam with barrier
res=line_plane_intersection(uaz,enemy,v1,v2,v3)
if res is None:
    print("HIT")
    sys.exit()
p,t=res
# intersection point must be between UAZ and enemy:
if not (0<=t<=1):
    print("HIT")
    sys.exit()
# check if intersection point inside triangle
if point_in_triangle(p,v1,v2,v3):
    print("MISS")
else:
    print("HIT")