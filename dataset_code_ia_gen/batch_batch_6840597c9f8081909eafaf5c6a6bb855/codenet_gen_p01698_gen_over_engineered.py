import sys
import math
from typing import List, Tuple, Optional

# Base vector in 3D with arithmetic
class Vector3D:
    __slots__ = ('x', 'y', 'z')
    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z
    def __add__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, scalar: float) -> 'Vector3D':
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)
    __rmul__ = __mul__
    def dot(self, other: 'Vector3D') -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z
    def norm2(self) -> float:
        return self.dot(self)
    def norm(self) -> float:
        return math.sqrt(self.norm2())

# Interface for objects that change over time
class DynamicObject:
    def position_at(self, t: float) -> Vector3D:
        raise NotImplementedError
    def radius_at(self, t: float) -> float:
        raise NotImplementedError
    def vanish_time(self) -> float:
        raise NotImplementedError

# Encapsulation of a shooting star as moving shrinking sphere
class ShootingStar(DynamicObject):
    __slots__ = ('index', 'pos0', 'v', 'r0', 'vr', 'vanish_t')
    def __init__(self, index: int, px: float, py: float, pz: float,
                 vx: float, vy: float, vz: float,
                 r: float, vr: float):
        self.index = index
        self.pos0 = Vector3D(px, py, pz)
        self.v = Vector3D(vx, vy, vz)
        self.r0 = r
        self.vr = vr
        self.vanish_t = r / vr  # natural vanish time
    def position_at(self, t: float) -> Vector3D:
        return self.pos0 + self.v * t
    def radius_at(self, t: float) -> float:
        return self.r0 - self.vr * t
    def vanish_time(self) -> float:
        return self.vanish_t

# Manager of interaction between multiple shooting stars
class ShootingStarSystem:
    def __init__(self, stars: List[ShootingStar]):
        self.stars = stars
        self.n = len(stars)
        # Store result vanish times considering collisions
        self.result_times: List[float] = [star.vanish_time() for star in stars]
        # Track if star is already vanished early because of collision
        self.collided: List[bool] = [False]*self.n
        # Precision tolerance
        self.EPS = 1e-14

    # Solve quadratic equation a*t^2 + b*t + c = 0 for roots >= 0, return smallest >=0 or None
    def solve_quadratic_nonneg(self, a: float, b: float, c: float) -> Optional[float]:
        if abs(a) < self.EPS:
            # Linear case bx + c = 0
            if abs(b) < self.EPS:
                return None
            t = -c / b
            return t if t >= -self.EPS else None
        d = b*b - 4*a*c
        if d < -self.EPS:
            return None
        d = max(d, 0.0)
        sqrt_d = math.sqrt(d)
        t1 = (-b - sqrt_d) / (2*a)
        t2 = (-b + sqrt_d) / (2*a)
        candidates = sorted([t for t in (t1,t2) if t >= -self.EPS])
        if not candidates:
            return None
        return candidates[0]

    # Compute collision time between two stars if any, else None
    def collision_time(self, i: int, j: int) -> Optional[float]:
        s1 = self.stars[i]
        s2 = self.stars[j]
        t_max = min(self.result_times[i], self.result_times[j])

        # Relative position and velocity
        dp = s1.pos0 - s2.pos0
        dv = s1.v - s2.v
        # Radius sum as function of t: (r1 - vr1 t) + (r2 - vr2 t) = (r1 + r2) - (vr1 + vr2) t
        r_sum0 = s1.r0 + s2.r0
        vr_sum = s1.vr + s2.vr

        # We want to find t >= 0 such that distance between centers = radius sum
        # (dp + dv t)^2 = (r_sum0 - vr_sum t)^2
        # Expand: (dp + dv t)^2 - (r_sum0 - vr_sum t)^2 = 0
        # => (dv•dv - vr_sum^2) t^2 + 2(dp•dv + r_sum0*vr_sum) t + (dp•dp - r_sum0^2) = 0
        a = dv.norm2() - vr_sum*vr_sum
        b = 2 * (dp.dot(dv) + r_sum0 * vr_sum)
        c = dp.norm2() - r_sum0*r_sum0

        t = self.solve_quadratic_nonneg(a,b,c)
        if t is None:
            return None
        if t < self.EPS:
            # Initial state no touching or overlapping per problem statement
            return None
        if t > t_max + self.EPS:
            return None
        # Check radius nonnegative at t:
        if s1.radius_at(t) < -self.EPS or s2.radius_at(t) < -self.EPS:
            return None
        # Check exact collision condition within numeric tolerances
        center_dist = (s1.position_at(t) - s2.position_at(t)).norm()
        radius_sum = s1.radius_at(t) + s2.radius_at(t)
        if abs(center_dist - radius_sum) > 1e-7:
            # Numerical instability or no exact tangency
            return None
        return t

    # Compute all collisions and update vanish times accordingly
    def compute_collisions(self):
        # Collect all possible collisions with their time
        events: List[Tuple[float,int,int]] = []
        for i in range(self.n):
            for j in range(i+1,self.n):
                t = self.collision_time(i,j)
                if t is not None:
                    events.append((t,i,j))
        # Sort by time ascending, for early collisions processed first
        events.sort()
        for t, i, j in events:
            if self.collided[i] or self.collided[j]:
                continue
            # If collision strictly before their current vanish time, update
            if t + self.EPS < self.result_times[i] and t + self.EPS < self.result_times[j]:
                self.result_times[i] = t
                self.result_times[j] = t
                self.collided[i] = True
                self.collided[j] = True

    def solve(self) -> List[float]:
        self.compute_collisions()
        return self.result_times

# Parsing utilities
def parse_floats(line: str) -> List[float]:
    return list(map(float,line.strip().split()))

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    output_lines = []
    while True:
        if idx >= len(input_lines):
            break
        nline = input_lines[idx].strip()
        idx += 1
        if not nline:
            continue
        n = int(nline)
        if n == 0:
            break
        stars: List[ShootingStar] = []
        for i in range(n):
            vals = parse_floats(input_lines[idx])
            idx += 1
            star = ShootingStar(i, *vals)
            stars.append(star)
        system = ShootingStarSystem(stars)
        vanish_times = system.solve()
        # Output formatted with strict 10 decimal places as required
        for t in vanish_times:
            output_lines.append(f"{t:.10f}")

    print("\n".join(output_lines))

if __name__ == "__main__":
    main()