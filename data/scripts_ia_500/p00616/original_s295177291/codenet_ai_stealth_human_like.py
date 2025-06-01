while True:
    n, h = map(int, input().split())
    if n == 0:
        break
    hit_positions = set()
    for _ in range(h):
        coord, a, b = input().split()
        a, b = int(a), int(b)
        if coord == 'xy':
            # all points with fixed x=a, y=b and varying z
            new_points = {(a, b, z) for z in range(1, n+1)}
        elif coord == 'xz':
            # vary y here
            new_points = {(a, y, b) for y in range(1, n+1)}
        elif coord == 'yz':
            # vary x here
            new_points = {(x, a, b) for x in range(1, n+1)}
        else:
            # unhandled coordinate system, just skip I guess
            new_points = set()
        hit_positions |= new_points  # union with existing hit points
    # total cubes minus the ones hit give the remaining cubes
    print(n**3 - len(hit_positions))