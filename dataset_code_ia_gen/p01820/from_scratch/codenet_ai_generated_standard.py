import sys
sys.setrecursionlimit(10**7)

n=int(sys.stdin.readline())
points=[]
dir_map={'>' : (1,0), 'v':(0,1), '<':(-1,0), '^':(0,-1)}
pos_dir_map={'>':0, 'v':1, '<':2, '^':3}

for i in range(n):
    x,y,d=sys.stdin.readline().split()
    x,y=int(x),int(y)
    points.append((x,y,d))

# Build next points: for each point and direction,
# find which point can be reached next

# We have directions encoded as 0:'>',1:'v',2:'<',3:'^'
# Proton moves along the direction, at speed 1 (or after acceleration speed doubled),
# but speed only influences how fast the proton moves along a line.
# However, the points have fixed coordinates.
# The proton starting from some point/vector combination must move towards the next point along direction vector.

# Since after each acceleration speed doubles but position moves at direction vector unit distance,
# the only possible sequence of points is those aligned strictly along the direction of movement.

# So for each point i and direction dir_i,
# find all points j where vector from point i to j is along direction dir_i and positive distance

# For each point, precompute the next point in the line in the given direction minimizing distance

# To do this efficiently, group points by coordinates projected on axis

from collections import defaultdict

# For directions, next possible points lie on line along direction d:
# For '>', x_j > x_i and y_j == y_i
# For 'v', y_j > y_i and x_j == x_i
# For '<', x_j < x_i and y_j == y_i
# For '^', y_j < y_i and x_j == x_i

x_map=defaultdict(list) # y->sorted list of (x, idx)
y_map=defaultdict(list) # x->sorted list of (y, idx)

for idx,(x,y,d) in enumerate(points):
    x_map[y].append((x,idx))
    y_map[x].append((y,idx))

for y in x_map:
    x_map[y].sort()
for x in y_map:
    y_map[x].sort()

# For each point and each direction, find next point on that line in that direction
# We'll store next_idx[point_idx][direction] = next point's idx or -1 if none
next_idx=[[-1]*4 for _ in range(n)]

for i,(x,y,d) in enumerate(points):
    # '>' dir=0
    arr=x_map[y]
    # find next point with x_j>x
    # binary search on arr
    import bisect
    pos=bisect.bisect_right(arr,(x,n))
    if pos<len(arr):
        next_idx[i][0]=arr[pos][1]

    # 'v' dir=1, next point y_j>y and x_j==x
    arr=y_map[x]
    pos=bisect.bisect_right(arr,(y,n))
    if pos<len(arr):
        next_idx[i][1]=arr[pos][1]

    # '<' dir=2, next point x_j < x and y_j==y
    arr=x_map[y]
    pos=bisect.bisect_left(arr,(x,-1))-1
    if pos>=0:
        next_idx[i][2]=arr[pos][1]

    # '^' dir=3, next point y_j < y and x_j==x
    arr=y_map[x]
    pos=bisect.bisect_left(arr,(y,-1))-1
    if pos>=0:
        next_idx[i][3]=arr[pos][1]

# Now dp with memo: dp[i][dir] = max #of ForcePoints accelerated starting from point i entering with direction dir
dp=[[-1]*4 for _ in range(n)]

def dfs(i,dir_in):
    if dp[i][dir_in]>=0:
        return dp[i][dir_in]
    # At point i, entering with direction dir_in,
    # proton is veered to direction points[i][2] (character)
    dchar=points[i][2]
    dir_out=pos_dir_map[dchar]
    ni=next_idx[i][dir_out]
    if ni==-1:
        dp[i][dir_in]=1
    else:
        dp[i][dir_in]=1+dfs(ni,dir_out)
    return dp[i][dir_in]

# The proton can start anywhere and with any direction,
# and any initial position (not necessarily at a Force Point).
# So the initial speed is 1, and the proton can be put at any coordinate and direction.
# To maximize acceleration, the proton must start at initial position so that the first Force Point is touched.
# Since the proton must touch a force point to increase speed,
# The maximum chain length is maximum over all points and incoming directions, plus zero accel if no point used.

res=0

for i in range(n):
    for dir_in in range(4):
        res=max(res,dfs(i,dir_in))

print(res)