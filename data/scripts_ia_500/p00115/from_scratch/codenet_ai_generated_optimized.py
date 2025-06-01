def dot(a,b): return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def sub(a,b): return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def same_side(p1,p2,a,b):
    cp1=cross(sub(b,a),sub(p1,a))
    cp2=cross(sub(b,a),sub(p2,a))
    return dot(cp1,cp2)>=0
def point_in_triangle(p,a,b,c):
    return (same_side(p,a,b,c) and same_side(p,b,a,c) and same_side(p,c,a,b))
def point_in_plane(p,a,b,c):
    n=cross(sub(b,a),sub(c,a))
    d=dot(n,sub(p,a))
    return abs(d)<1e-9
def main():
    A=tuple(map(int,input().split()))
    E=tuple(map(int,input().split()))
    P1=tuple(map(int,input().split()))
    P2=tuple(map(int,input().split()))
    P3=tuple(map(int,input().split()))
    # 敵がバリア内にいるか判定
    if point_in_plane(E,P1,P2,P3) and point_in_triangle(E,P1,P2,P3):
        print("MISS")
        return
    # ビームの方向ベクトル
    d=sub(E,A)
    n=cross(sub(P2,P1),sub(P3,P1))
    denom=dot(n,d)
    # 平行なら衝突しない
    if denom==0:
        print("HIT")
        return
    t=dot(n,sub(P1,A))/denom
    # t<0なら交差はA側にあるので MISSしない
    if t<0 or t>1:
        print("HIT")
        return
    # 交点座標
    I=(A[0]+d[0]*t,A[1]+d[1]*t,A[2]+d[2]*t)
    # 交点がバリア内か
    if point_in_triangle(I,P1,P2,P3):
        print("MISS")
    else:
        print("HIT")
main()