import sys
input=sys.stdin.readline

W,H=map(int,input().split())
N=int(input())
X=[0]*N
Y=[0]*N
for i in range(N):
    x,y=map(int,input().split())
    X[i]=x
    Y[i]=y

X.sort()
Y.sort()

if N%2==1:
    median_x = X[N//2]
    median_y = Y[N//2]
else:
    median_x_candidates = [X[N//2-1], X[N//2]]
    median_y_candidates = [Y[N//2-1], Y[N//2]]

def total_dist(coord_list, c):
    # sum of |x_i - c|
    return sum(abs(x - c) for x in coord_list)

if N%2==1:
    x_best = median_x
    y_best = median_y
else:
    # For even N, check all median candidates and pick one that yields minimal total distance
    # Also consider tie-breaks as required
    # For x
    x_candidates = median_x_candidates
    # For y
    y_candidates = median_y_candidates

    min_dist = None
    x_best = None
    y_best = None
    for x_c in x_candidates:
        for y_c in y_candidates:
            dist = 2*(total_dist(X,x_c)+total_dist(Y,y_c))
            if (min_dist is None) or (dist < min_dist) or (dist == min_dist and (x_c < x_best or (x_c==x_best and y_c<y_best))):
                min_dist = dist
                x_best = x_c
                y_best = y_c

# Calculate total minimal time
total = 2*(sum(abs(x - x_best) for x in X) + sum(abs(y - y_best) for y in Y))

print(total)
print(x_best,y_best)