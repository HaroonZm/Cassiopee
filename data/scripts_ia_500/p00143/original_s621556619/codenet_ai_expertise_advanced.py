from sys import stdin

def check(triangle, pt):
    v = [tuple(triangle[i:i+2]) for i in range(0, 6, 2)]
    sign = lambda p1, p2, p3: (p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0]-p3[0])*(p1[1]-p3[1])
    b = [sign(pt, v[i], v[(i+1)%3]) > 0 for i in range(3)]
    return all(b) or not any(b)

input_iter = iter(stdin.read().split())
n = int(next(input_iter))

for _ in range(n):
    data = list(map(int, (next(input_iter) for __ in range(10))))
    triangle, hikoboshi, orihime = data[:6], tuple(data[6:8]), tuple(data[8:10])
    print("OK" if check(triangle, hikoboshi) ^ check(triangle, orihime) else "NG")