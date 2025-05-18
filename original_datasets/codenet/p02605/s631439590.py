N = int(input())
plane = [0] * N
houkou = ["U", "D", "R", "L"]
up = []
down = []
right = []
left =[]
for i in range(N):
  x, y, p = list(map(str, input().split()))
  x = int(x)
  y = int(y)
  p2 = houkou.index(p)
  plane[i] = [x, y, x + y, x - y, p2]
  
#x座標が同じでぶつかる
plane = sorted(plane, key=lambda x:x[1])
plane = sorted(plane, key=lambda x:x[0])
#print(plane)
time = 10 ** 10
for k in range(1, N):
    if plane[k][0] == plane[k - 1][0]:
      if plane[k][1] > plane[k - 1][1]:
        if (plane[k][4] == 1) and (plane[k - 1][4] == 0):
          time2 = (plane[k][1] - plane[k - 1][1]) / 0.2
          time = min(time, time2)
      else:
        if (plane[k][4] == 0) and (plane[k - 1][4] == 1):
          time2 = (plane[k - 1][1] - plane[k][1]) / 0.2
          time = min(time, time2)
        
#y座標が同じでぶつかる
plane = sorted(plane, key=lambda x:x[0])
plane = sorted(plane, key=lambda x:x[1])
for k in range(1, N):
    if plane[k][1] == plane[k - 1][1]:
      if plane[k][0] > plane[k - 1][0]:
        if (plane[k][4] == 3) and (plane[k - 1][4] == 2):
          time2 = (plane[k][0] - plane[k - 1][0]) / 0.2
          time = min(time, time2)
      else:
        if (plane[k][4] == 2) and (plane[k - 1][4] == 3):
          time2 = (plane[k - 1][0] - plane[k][0]) / 0.2
          time = min(time, time2)

def go(x, y, u, t):
  if u == 0:
    return x, int(y + t * 0.1)
  elif u== 1:
    return x, int(y - t * 0.1)
  elif u == 2:
    return int(x + t * 0.1), y
  else:
    return int(x - t * 0.1), y
  
          
#和が同じでぶつかる
plane = sorted(plane, key=lambda x:x[2])
for k in range(1, N):
    one = plane[k]
    two = plane[k - 1]
                
    if plane[k][2] == plane[k - 1][2]:
      time2 = abs(one[0] - two[0]) / 0.1
      max_x = max(one[0],two[0])
      min_x = min(one[0], two[0])
      max_y = max(one[1], two[1])
      min_y = min(one[1], two[1])
      L = [[max_x, max_y], [min_x, min_y]]
      #k
      k_x, k_y = go(one[0], one[1], one[4], time2)
      #k - 1
      k2_x, k2_y = go(two[0], two[1], two[4], time2)
      if [k_x, k_y] in L:
        if [k2_x, k2_y] in L:
          if [k_x, k_y] == [k2_x, k2_y]:
            time = min(time, time2)
          
#差が同じでぶつかる
plane = sorted(plane, key=lambda x:x[3])
#print(plane)
for k in range(1, N):
    one = plane[k]
    two = plane[k - 1]
                
    if plane[k][3] == plane[k - 1][3]:
      time2 = abs(one[0] - two[0]) / 0.1
      max_x = max(one[0],two[0])
      min_x = min(one[0], two[0])
      max_y = max(one[1], two[1])
      min_y = min(one[1], two[1])
      L = [[max_x, min_y], [min_x, max_y]]
      #k
      k_x, k_y = go(one[0], one[1], one[4], time2)
      #k - 1
      k2_x, k2_y = go(two[0], two[1], two[4], time2)
      if [k_x, k_y] in L:
        if [k2_x, k2_y] in L:
          if [k_x, k_y] == [k2_x, k2_y]:
            time = min(time, time2)          
            
if time == 10 ** 10:
  print("SAFE")
else:
  print(int(time))
#print(plane)