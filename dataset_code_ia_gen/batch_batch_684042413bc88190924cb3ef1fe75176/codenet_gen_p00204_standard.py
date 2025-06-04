import sys
import math

def dist(x, y):
    return math.sqrt(x*x + y*y)

for line in sys.stdin:
    if not line.strip():
        continue
    R, N = map(int, line.split())
    if R == 0 and N == 0:
        break
    ufos = []
    for _ in range(N):
        x0, y0, r, v = map(int, sys.stdin.readline().split())
        ufos.append([x0, y0, r, v])
    time = 1
    downed = set()
    while True:
        # positions of UFOs not downed yet
        positions = []
        for i, (x0, y0, r, v) in enumerate(ufos):
            if i in downed:
                continue
            x = x0 - v * time * (x0 / dist(x0, y0))
            y = y0 - v * time * (y0 / dist(x0, y0))
            positions.append((dist(x, y), i, x, y, r))
        # select target: the nearest UFO outside R at this time
        candidates = [(d, i, x, y, r) for (d,i,x,y,r) in positions if d > R]
        if not candidates:
            break
        target = min(candidates, key=lambda x: x[0])
        laser_dist, idx, tx, ty, tr = target
        # laser kills all UFOs intersected by the laser line passing through the target
        # laser line: center to origin (0,0), direction vector (tx,ty)
        # For each UFO, check if line from origin to target intersects it
        # Because laser is fired along direction of target
        # Actually laser is a ray from origin in direction of target
        # We check UFOs whose center projections along laser are >=0 and distance to laser line <= UFO radius
        # And with center distance at the shot time more than R (?)
        for i, (x0, y0, r, v) in enumerate(ufos):
            if i in downed:
                continue
            x = x0 - v * time * (x0 / dist(x0, y0))
            y = y0 - v * time * (y0 / dist(x0, y0))
            # Project point on laser direction
            d_origin = math.sqrt(tx*tx + ty*ty)
            dot = x*tx + y*ty
            if dot < 0:
                continue
            proj_len = dot / d_origin
            # perpendicular distance to laser line
            perp_dist = math.sqrt((x* x + y*y) - proj_len*proj_len)
            if perp_dist <= r:
                downed.add(i)
        time += 1

    # count UFOs within R at any time point? No, only remaining UFOs that got inside R at the end.
    # Because simulation runs until no more targets outside R,
    # remaining UFOs are inside R since otherwise they could be targeted.
    count = 0
    for i, (x0, y0, r, v) in enumerate(ufos):
        if i in downed:
            continue
        # check distance when UFO reaches radius R to detect if it entered the range
        d0 = dist(x0, y0)
        if d0 <= R:
            count += 1
        else:
            # calculate time to reach distance R
            t_enter = (d0 - R)/v
            # if UFO is still alive after simulation time, it means it has entered inside R
            # since simulation ends when no UFO is outside R to shoot.
            # Actually, the problem states to count UFOs inside R after all shots
            # So all alive UFOs must be inside R.
            count += 1
    print(count)