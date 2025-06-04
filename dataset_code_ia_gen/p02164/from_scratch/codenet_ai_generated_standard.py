import sys, math, itertools
input=sys.stdin.readline
N=int(input())
shops=[tuple(map(int,input().split())) for _ in range(N)]
points=[(0,0)]+shops

def angle_between(u,v):
    ux,uy=u
    vx,vy=v
    dot=ux*vx+uy*vy
    det=ux*vy-uy*vx
    a=math.atan2(det,dot)
    return a

def dist(a,b):
    return math.hypot(b[0]-a[0],b[1]-a[1])

min_angle=float('inf')
for perm in itertools.permutations(range(1,N+1)):
    angle_sum=0
    dir_vector=(1,0)
    pos=(0,0)
    path=[0]+list(perm)+[0]
    for i in range(1,len(path)):
        next_pos=points[path[i]]
        move_vec=(next_pos[0]-pos[0], next_pos[1]-pos[1])
        if move_vec==(0,0):
            turn_angle=0
        else:
            turn_angle=abs(math.degrees(angle_between(dir_vector,move_vec)))
        angle_sum+=turn_angle
        dir_vector=move_vec if move_vec!=(0,0) else dir_vector
        pos=next_pos
    if angle_sum<min_angle:
        min_angle=angle_sum
print(f"{min_angle:.9f}")