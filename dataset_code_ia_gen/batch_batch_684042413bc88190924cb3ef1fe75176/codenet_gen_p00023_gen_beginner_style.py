N = int(input())
for _ in range(N):
    xa, ya, ra, xb, yb, rb = map(float, input().split())
    dx = xa - xb
    dy = ya - yb
    dist = (dx*dx + dy*dy)**0.5
    
    if dist + rb < ra:
        print(2)
    elif dist + ra < rb:
        print(-2)
    elif dist <= ra + rb and dist >= abs(ra - rb):
        print(1)
    else:
        print(0)