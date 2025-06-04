import sys
import math

def polygon_area(v_list):
    angles = v_list + [360 - sum(v_list)]
    r = 1
    s = 0
    for i in range(len(angles)):
        a = math.radians(angles[i])
        b = math.radians(angles[(i+1)%len(angles)])
        s += math.sin(a + b) - math.sin(b)
    area = 0.5 * r * r * abs(s)
    return area

input = sys.stdin.read().strip().split()
idx = 0
while True:
    if idx >= len(input):
        break
    m = int(input[idx])
    idx += 1
    if m == 0:
        break
    v1 = list(map(int, input[idx:idx+m-1]))
    idx += m-1
    n = int(input[idx])
    idx += 1
    v2 = list(map(int, input[idx:idx+n-1]))
    idx += n-1
    a1 = polygon_area(v1)
    a2 = polygon_area(v2)
    if abs(a1-a2) < 1e-10:
        print(0)
    elif a1 > a2:
        print(1)
    else:
        print(2)