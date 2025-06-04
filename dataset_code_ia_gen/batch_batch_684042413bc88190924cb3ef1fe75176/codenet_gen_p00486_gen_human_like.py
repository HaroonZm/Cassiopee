import sys
input = sys.stdin.readline

W,H = map(int,input().split())
N = int(input())
X = []
Y = []
for _ in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()

# 中央値の取得
if N%2 == 1:
    median_x = X[N//2]
    median_y = Y[N//2]
else:
    median_x_candidates = [X[N//2 - 1], X[N//2]]
    median_y_candidates = [Y[N//2 - 1], Y[N//2]]
    median_x = min(median_x_candidates)
    median_y = min(median_y_candidates)

# 移動時間の計算
total_time = 0
for i in range(N):
    dist = abs(X[i]-median_x)+abs(Y[i]-median_y)
    total_time += 2*dist

print(total_time)
print(median_x, median_y)