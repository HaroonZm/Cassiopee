# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections
N,E = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
#sdw = [[src1 dist1 d1][src1 dist1 d1]...]# vect source1 -> distance1 distances
INF = float("inf")
ALL = set(range(N))

distances = [[INF]*N for _ in range(N)]
for i in range(N):
  distances[i][i] = 0

for i in range(E):
  s,d,w = (map(int,sys.stdin.readline().rstrip().split()))
  distances[s][d] = w

#print(distances)
def warshallFloyd():
  for k in range(N):
    for i in range(N):
      for j in range(N):
        distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

warshallFloyd()

for i in range(N):
  if distances[i][i] < 0:
    print("NEGATIVE CYCLE")
    exit()

for i in range(N):
  s = []
  for j in range(N):
    if distances[i][j] == INF:
      s.append("INF")
    else:
      s.append(str(distances[i][j]))
  print(" ".join(s))