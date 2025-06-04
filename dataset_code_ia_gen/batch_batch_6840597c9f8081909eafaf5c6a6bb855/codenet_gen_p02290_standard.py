import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
q = int(input())

dx, dy = x2 - x1, y2 - y1
den = dx*dx + dy*dy

for _ in range(q):
    px, py = map(int, input().split())
    t = ((px - x1)*dx + (py - y1)*dy) / den
    x = x1 + t*dx
    y = y1 + t*dy
    print(f"{x:.10f} {y:.10f}")