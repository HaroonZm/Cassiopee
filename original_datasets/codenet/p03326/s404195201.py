n, m = [int(item) for item in input().split()]
xyz = [[int(item) for item in input().split()] for _ in range(n)]

values = [[0] * n for _ in range(8)]

sign = [[1,1,1],
        [1,1,-1],
        [1,-1,1],
        [-1,1,1],
        [-1,-1,1],
        [-1,1,-1],
        [1,-1,-1],
        [-1,-1,-1]]

for i, (x, y, z) in enumerate(xyz):
  for j in range(8):
    values[j][i] += x * sign[j][0]
    values[j][i] += y * sign[j][1]
    values[j][i] += z * sign[j][2]

if m == 0:
  print(0)
else:
  ans = 0
  for line in values:
    ans = max(ans, sum(sorted(line)[-m:]))
  print(ans)