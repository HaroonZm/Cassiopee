import sys
import math
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# Collect unique x and y coordinates with weights sum per coordinate
from collections import defaultdict

sum_x = defaultdict(int)
sum_y = defaultdict(int)
total = 0
for x, y, w in points:
    sum_x[x] += w
    sum_y[y] += w
    total += w

X = sorted(sum_x.items())
Y = sorted(sum_y.items())

# Prefix sums for x and y
px = [0]
for _, w in X:
    px.append(px[-1] + w)
py = [0]
for _, w in Y:
    py.append(py[-1] + w)

max_num = 0
max_den = 1

# We want to find two sensors at lattice points with different x and y.
# The rectangle sides are |x1-x2| and |y1-y2|
# The numerator is sum of weights inside rectangle, we want max numerator/area.

# For optimization, consider only min and max in x and y as candidates because other intervals will have larger area for less gain.
# But we can also check combined extrema:

# Precompute total sums for quick access
sumX = [0]*(len(X)+1)
for i in range(len(X)):
    sumX[i+1] = sumX[i] + X[i][1]
sumY = [0]*(len(Y)+1)
for i in range(len(Y)):
    sumY[i+1] = sumY[i] + Y[i][1]

# Map x and y to index for further processing
x_to_idx = {x:i for i,(x,_) in enumerate(X)}
y_to_idx = {y:i for i,(y,_) in enumerate(Y)}

# We will iterate over all pairs of distinct x and y coordinates,
# but that is too big O(N^2).

# Alternative approach:
# For each pair of distinct x coordinates (x1,x2), consider total foxes in that x range at all y's,
# and then find y coordinates giving best ratio of sum/(x_dist * y_dist).

# Because points are unique but foxes count can be many at point,
# let's build a 2D grid with weights per (x_idx,y_idx):

w_grid = [[0]*len(Y) for _ in range(len(X))]
for x, y, w in points:
    xi = x_to_idx[x]
    yi = y_to_idx[y]
    w_grid[xi][yi] = w

# Build 2D prefix sums for fast rectangle sum queries
ps = [[0]*(len(Y)+1) for _ in range(len(X)+1)]
for i in range(len(X)):
    row_sum = 0
    for j in range(len(Y)):
        row_sum += w_grid[i][j]
        ps[i+1][j+1] = ps[i][j+1] + row_sum

def rect_sum(x1i,x2i,y1i,y2i):
    return ps[x2i+1][y2i+1]-ps[x1i][y2i+1]-ps[x2i+1][y1i]+ps[x1i][y1i]

max_a = 0
max_b = 1

# We try to find a rectangle maximizing sum/(width*height)
# Enumerate all pairs (x1i,x2i), where x1i < x2i
# For each, find the best y interval
# For fixed x interval, for each y interval we compute sum and area, maximize ratio.

# Because N can be 1e5, O(N^3) is impossible
# So we use a sliding approach:
# For each fixed x interval, we use two pointers on y coords to find best y interval with max sum/(width*height)

for x1i in range(len(X)-1):
    for x2i in range(x1i+1,len(X)):
        width = X[x2i][0] - X[x1i][0]
        # Extract line of sums for current x interval for all y
        arr = [rect_sum(x1i,x2i,y,y) for y in range(len(Y))]
        # Use two pointers to find max ratio sum/(width*height)
        # height = Y[r] - Y[l]
        l = 0
        s = arr[0]
        for r in range(1,len(Y)):
            s += arr[r]
            while l < r and s*(Y[r][0] - Y[l+1][0]) > s*(Y[r][0] - Y[l][0]):
                s -= arr[l]
                l += 1
            height = Y[r][0] - Y[l][0]
            if height == 0:
                continue
            num = s
            den = width * height
            # Check if num/den > max_a/max_b
            # Compare cross products to avoid float
            if num * max_b > max_a * den:
                max_a, max_b = num, den

# If no rectangle found (max_a=0), print 0 / 1
if max_a == 0:
    print("0 / 1")
else:
    g = math.gcd(max_a, max_b)
    print(f"{max_a//g} / {max_b//g}")