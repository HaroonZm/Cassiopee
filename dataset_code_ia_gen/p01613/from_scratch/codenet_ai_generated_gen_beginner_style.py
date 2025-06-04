n = int(input())
a, b = map(int, input().split())
c, d = map(int, input().split())

min_distance = None

for w in range(1, n+1):
    # Calculer les positions des 4 usines pour cette largeur w
    ax, ay = (a - 1) % w, (a - 1) // w
    bx, by = (b - 1) % w, (b - 1) // w
    cx, cy = (c - 1) % w, (c - 1) // w
    dx, dy = (d - 1) % w, (d - 1) // w

    dist = abs(ax - bx) + abs(ay - by) + abs(cx - dx) + abs(cy - dy)

    if min_distance is None or dist < min_distance:
        min_distance = dist

print(min_distance)