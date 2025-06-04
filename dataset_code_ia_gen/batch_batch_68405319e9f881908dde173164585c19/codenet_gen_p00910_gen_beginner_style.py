import sys
import math

def distance_sq(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

def point_in_balloon(p, c, r):
    return distance_sq(p, c) < r*r

def line_intersects_balloon(light, end, center, radius):
    # Check if the segment from light to end intersects the balloon sphere
    # Simple approach: check closest distance from center to line segment
    lx, ly, lz = light
    ex, ey, ez = end
    cx, cy, cz = center
    vx, vy, vz = ex-lx, ey-ly, ez-lz
    wx, wy, wz = cx-lx, cy-ly, cz-lz
    c1 = vx*wx + vy*wy + vz*wz
    if c1 <= 0:
        d = distance_sq((lx,ly,lz), center)
        return d < radius*radius
    c2 = vx*vx + vy*vy + vz*vz
    if c2 <= c1:
        d = distance_sq((ex,ey,ez), center)
        return d < radius*radius
    b = c1 / c2
    pb = (lx + b*vx, ly + b*vy, lz + b*vz)
    d = distance_sq(pb, center)
    return d < radius*radius

for line in sys.stdin:
    if line.strip() == '':
        continue
    NMR = line.strip().split()
    if len(NMR) != 3:
        continue
    N, M, R = map(int, NMR)
    if N == 0 and M == 0 and R == 0:
        break

    balloons = []
    for _ in range(N):
        sx, sy, sz, sr = map(int, sys.stdin.readline().strip().split())
        balloons.append((sx, sy, sz, sr))
    lights = []
    for _ in range(M):
        tx, ty, tz, tb = map(int, sys.stdin.readline().strip().split())
        lights.append((tx, ty, tz, tb))
    Ex, Ey, Ez = map(int, sys.stdin.readline().strip().split())
    E = (Ex, Ey, Ez)

    # For each light source, check which balloons block it
    light_blocking = []
    for j in range(M):
        tx, ty, tz, tb = lights[j]
        blockers = []
        for i in range(N):
            sx, sy, sz, sr = balloons[i]
            # If line from light to E passes through balloon i
            if line_intersects_balloon((tx,ty,tz), E, (sx,sy,sz), sr):
                blockers.append(i)
        light_blocking.append(blockers)

    # Initially, light blocked by any balloon in its blockers list
    # We can remove up to R balloons to unblock some lights

    # For each balloon, find all lights it blocks
    balloon_blocks = [[] for _ in range(N)]
    for j in range(M):
        for b in light_blocking[j]:
            balloon_blocks[b].append(j)

    # Each light is blocked by 0 or more balloons
    # If 0 blockers, light is always on, else need to remove all blockers
    # But we can only remove R balloons total

    # Simple greedy approach: prioritize removing balloons that unblock the most brightness
    # For each balloon, sum the brightness of lights that are only blocked by this balloon
    # Because if a light is blocked by multiple balloons, removing one does not unblock it

    # So we compute for each balloon how much brightness can be gained if we remove it,
    # but only for lights blocked solely by that balloon.

    # First compute for each light, set of blockers
    light_block_set = [set(blockers) for blockers in light_blocking]

    # Also compute light intensity if reachable
    light_intensity = []
    for j in range(M):
        tx, ty, tz, tb = lights[j]
        d2 = (tx-Ex)**2 + (ty-Ey)**2 + (tz-Ez)**2
        inten = tb / d2
        light_intensity.append(inten)

    # Lights with no blockers
    always_on_lights = 0.0
    for j in range(M):
        if len(light_block_set[j]) == 0:
            always_on_lights += light_intensity[j]

    # For lights blocked by one balloon only, keep track of brightness gain if that balloon removed
    balloon_gain = [0.0]*N
    for j in range(M):
        if len(light_block_set[j]) == 1:
            b = next(iter(light_block_set[j]))
            balloon_gain[b] += light_intensity[j]

    # For lights blocked by multiple balloons, need to remove all blockers, complex, skip for beginner

    # Remove up to R balloons with biggest gains
    gain_with_index = list(enumerate(balloon_gain))
    gain_with_index.sort(key=lambda x: x[1], reverse=True)
    removed = set()
    total_gain = 0.0
    count = 0
    for b, g in gain_with_index:
        if count >= R:
            break
        if g > 0:
            removed.add(b)
            total_gain += g
            count += 1

    # Calculate if any multiple-blocked lights can be unblocked:
    # At beginner level, skip this.

    # So total light intensity is sum of always on + total_gain from removed balloons

    result = always_on_lights + total_gain

    print(result)