import sys

input_line = sys.stdin.readline()
n, r, l = map(int, input_line.split())

appearance = [0] * n
point = [0] * n

top = 0
previous_time = 0

for line in sys.stdin:
    d_str, t_str, x_str = line.split()
    d = int(d_str) - 1
    t = int(t_str)
    x = int(x_str)

    appearance[top] += t - previous_time
    previous_time = t

    point[d] += x

    if x > 0 and top != d:
        if point[d] > point[top]:
            top = d
        elif point[d] == point[top]:
            if d < top:
                top = d
    elif x < 0 and top == d:
        max_points = max(point)
        top = point.index(max_points)

appearance[top] += l - previous_time

result = 1 + appearance.index(max(appearance))
print(result)