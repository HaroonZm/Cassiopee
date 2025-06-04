def read_line():
    return list(map(int, input().split()))
    
CONST_1 = 1e21
rng = range

n, m = read_line()
FaRb = [-CONST_1, CONST_1]
xs, ys = {0, -CONST_1, CONST_1}, {0, -CONST_1, CONST_1}

R = [((-CONST_1, CONST_1), CONST_1), ((-CONST_1, CONST_1), -CONST_1)]
H = [(CONST_1, (-CONST_1, CONST_1)), (-CONST_1, (-CONST_1, CONST_1))]

for _ in rng(n):
    a, b, c = read_line()
    R.append(((a,b),c))
    ys.add(c)
    xs.update([a,b])

for _ in rng(m):
    a, b, c = read_line()
    H.append((a, (b, c)))
    xs.add(a)
    ys.update([b,c])

sorted_x, sorted_y = sorted(xs), sorted(ys)
x_id = {x:i for i,x in enumerate(sorted_x)}
y_id = {y:i for i,y in enumerate(sorted_y)}

K, L = len(sorted_x), len(sorted_y)

def make_grid(): return [[0]*(K+1) for _ in range(L+1)]
U = make_grid()
V = make_grid()
u = [[0]*(K+1) for _ in rng(L+1)]
for ((a, b), c) in R:
    U[y_id[c]][x_id[a]] += 1
    U[y_id[c]][x_id[b]] -= 1

for i in rng(L):
    j = 0
    while j < K:
        U[i][j+1] += U[i][j]
        j += 1

for d, (e, f) in H:
    V[y_id[e]][x_id[d]] += 1
    V[y_id[f]][x_id[d]] -= 1

for j in range(K):
    for i in range(L):
        V[i+1][j] += V[i][j]
        
visited = [[False]*(K+1) for _ in rng(L+1)]
X_QUEUE = []
h0, w0 = x_id[0], y_id[0]
X_QUEUE.append((h0,w0))
visited[w0][h0] = True
answer = 0
while X_QUEUE:
    x, y = X_QUEUE.pop()
    answer += (sorted_x[x]-sorted_x[x+1])*(sorted_y[y]-sorted_y[y+1])
    for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
        nx, ny = x+dx, y+dy
        # mixed logic style for bounds/visits
        if 0 <= nx < K and 0 <= ny < L and not visited[ny][nx]:
            if (U[(dy>0)+y][x] == 0 or dx == 0) and (V[y][(dx>0)+x] == 0 or dy == 0):
                X_QUEUE.append((nx,ny))
                visited[ny][nx]=1

if answer > CONST_1:
    answer = 'INF'
print(answer)