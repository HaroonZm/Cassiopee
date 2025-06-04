import sys
import math

def dist(x, y):
    return math.sqrt(x*x + y*y)

def will_enter_range(R, x0, y0, r, v):
    # UFO moves straight toward origin (0,0)
    # initial distance from origin to center
    d0 = dist(x0, y0)
    # Time when UFO enters the laser non-power range (distance <= R)
    # If initial distance already <= R, then enters at t=0
    # UFO moves linearly toward origin at speed v (units per minute)
    # Distance from origin at time t: d(t) = max(0, d0 - v * t)
    # Solve for time t when d(t) <= R => d0 - v*t <= R => t >= (d0 - R)/v
    # If (d0 - R)/v <=0, then UFO is already inside at start
    enter_time = max(0, (d0 - R)/v)

    # Laser fires first at t=1, then every minute: t=1,2,3,...
    # At each laser firing time, find the closest UFO at that time,
    # and fire a laser that kills that UFO plus others on the same line.
    # UFOs inside R never targeted, so they remain intact.

    # We only want to know if UFO escapes being shot and enters R area.
    # If UAV is shot before it enters R area, it does not count.
    # If UAV enters R area before being shot, it counts.

    return enter_time

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        R_N = line.split()
        if len(R_N) < 2:
            continue
        R, N = map(int, R_N)
        if R == 0 and N == 0:
            break
        ufos = []
        for _ in range(N):
            x0, y0, r, v = map(int, input().split())
            ufos.append([x0, y0, r, v, False])  # last False means alive

        # We simulate time starting from t=1 for laser shots, each minute.
        # Laser fires at t=1, 2, 3, ... as long as there are targets outside R.
        # For each firing, find closest UFO (distance - r) > R among all alive UFOs.
        # Shoot it and all other UFOs that lie on the same inf line from origin.
        # Mark all those UFOs as killed.

        # Shoot until no UFO alive outside power=R range.

        time = 1
        while True:
            candidates = []
            for i, (x0, y0, r, v, dead) in enumerate(ufos):
                if dead:
                    continue
                # Position at time t: move toward origin distance v*t
                # Current distance to origin = max(0, d0 - v*t)
                d0 = dist(x0, y0)
                d = max(0, d0 - v * time)
                # If d <= R, not targetable
                if d <= R:
                    continue
                # Distance from origin to edge closest to origin: d - r
                dist_edge = d - r
                candidates.append((dist_edge, i, d, x0, y0))

            if not candidates:
                break

            # Get the closest UFO (by dist_edge)
            candidates.sort()
            _, target_i, target_d, tx0, ty0 = candidates[0]

            # Position of target at time t
            d0, d1 = dist(tx0, ty0), max(0, dist(tx0, ty0) - ufos[target_i][3] * time)
            # Unit vector from origin to target position at time t
            # Position is at distance d1 along vector (x0,y0)
            # compute position at time t:
            x0_, y0_, r_, v_, dead_ = ufos[target_i]
            d0 = dist(x0_, y0_)
            if d0 == 0:
                px, py = 0, 0
            else:
                move_dist = min(d0, v_ * time)
                px = x0_ * (max(0, d0 - move_dist) / d0)
                py = y0_ * (max(0, d0 - move_dist) / d0)

            # Direction vector of the laser line from origin to (px, py)
            # We kill all UFOs whose centers at time t lie on the same line from origin.
            # To check collinearity, the cross product should be 0 (or close),
            # and dot product > 0 to be in same direction.

            # Mark all UFOs on this line as dead
            for j, (x0j, y0j, rj, vj, deadj) in enumerate(ufos):
                if deadj:
                    continue
                d0j = dist(x0j, y0j)
                d_j = max(0, d0j - vj * time)
                if d_j <= R:
                    continue
                # Position at time t
                if d0j == 0:
                    pjx, pjy = 0, 0
                else:
                    move_dist_j = min(d0j, vj * time)
                    pjx = x0j * (max(0, d0j - move_dist_j) / d0j)
                    pjy = y0j * (max(0, d0j - move_dist_j) / d0j)
                # cross product of (px,py) x (pjx,pjy) = px*pjy - py*pjx
                cross = px * pjy - py * pjx
                # dot product (for same direction)
                dot = px * pjx + py * pjy
                if abs(cross) < 1e-10 and dot > 0:
                    ufos[j][4] = True  # killed
            time += 1

        # Count UFO inside R radius (distance to origin <= R) after unlimited time
        # Also those that could never be shot.
        count = 0
        # We need to check which UFOs eventually enter R area alive
        # For each UFO not killed, calculate enter time, and if finite, count it.
        for x0, y0, r, v, dead in ufos:
            if dead:
                continue
            d0 = dist(x0, y0)
            enter_t = max(0, (d0 - R) / v)
            # If enter_t is finite (which it always is) => UFO will be inside R undestroyed
            # That means UFO is counted
            count += 1

        print(count)

if __name__ == "__main__":
    main()