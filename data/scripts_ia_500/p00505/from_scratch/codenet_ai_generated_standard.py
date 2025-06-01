import sys

count_triangle = 0
count_right = 0
count_acute = 0
count_obtuse = 0

for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) < 3:
        continue
    try:
        a, b, c = map(int, parts[:3])
    except:
        continue
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        print(count_triangle, count_right, count_acute, count_obtuse)
        break
    count_triangle += 1
    sq = [x*x for x in sides]
    if sq[0] + sq[1] == sq[2]:
        count_right += 1
    elif sq[0] + sq[1] > sq[2]:
        count_acute += 1
    else:
        count_obtuse += 1