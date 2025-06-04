import io, sys
import bisect

N = int(sys.stdin.readline())
x1y1x2y2_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
X1 = [a for a, b, c, d in x1y1x2y2_list]
X2 = [c for a, b, c, d in x1y1x2y2_list]
Y1 = [b for a, b, c, d in x1y1x2y2_list]
Y2 = [d for a, b, c, d in x1y1x2y2_list]

all_X = []
for a in X1 + X2:
    all_X.append(a)
all_X = sorted(set(all_X))
for i in range(len(X1)):
    X1[i] = bisect.bisect_left(all_X, X1[i])
    X2[i] = bisect.bisect_left(all_X, X2[i])

all_Y = []
for a in Y1 + Y2:
    all_Y.append(a)
all_Y = sorted(set(all_Y))
for i in range(len(Y1)):
    Y1[i] = bisect.bisect_left(all_Y, Y1[i])
    Y2[i] = bisect.bisect_left(all_Y, Y2[i])

matrix = [ [0] * len(all_X) for _ in range(len(all_Y)) ]
for i in range(N):
    matrix[Y1[i]][X1[i]] += 1
    matrix[Y2[i]][X2[i]] += 1
    matrix[Y2[i]][X1[i]] -= 1
    matrix[Y1[i]][X2[i]] -= 1

for row in range(len(matrix)):
    for col in range(1, len(matrix[0])):
        matrix[row][col] += matrix[row][col-1]

for row in range(1, len(matrix)):
    for col in range(len(matrix[0])):
        matrix[row][col] += matrix[row-1][col]

ans = 0
for row in range(len(matrix)-1):
    for col in range(len(matrix[0])-1):
        if matrix[row][col] > 0:
            area = (all_X[col+1] - all_X[col]) * (all_Y[row+1] - all_Y[row])
            ans += area

print(ans)