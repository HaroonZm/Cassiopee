import math

PI=3.1415926535897932384626433832795
M=PI/180.0

def distance(y1,x1,y2,x2):
    cos = math.cos
    sin = math.sin
    acos = math.acos
    a = cos(y1*M)*cos(y2*M)*cos((x1-x2)*M) + sin(y1*M)*sin(y2*M)
    return int(6378.1*acos(a) + 0.5)

def main():
    while True:
        coords = input().strip().split()
        y1, x1, y2, x2 = map(float, coords)
        if all(val == -1 for val in (x1,y1,x2,y2)): return
        print(distance(y1,x1,y2,x2))

main()