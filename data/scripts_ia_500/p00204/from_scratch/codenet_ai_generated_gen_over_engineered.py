import sys
import math
from typing import List, Optional, Tuple

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def norm(self) -> float:
        return math.hypot(self.x, self.y)

    def scaled(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

    def sub(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def add(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def normalized(self) -> 'Vector2D':
        n = self.norm()
        if n == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / n, self.y / n)

class UFO:
    def __init__(self, pos: Vector2D, radius: float, speed: float):
        self.pos = pos
        self.radius = radius
        self.speed = speed
        self.alive = True

    def position_at(self, minute: float) -> Vector2D:
        # UFO moves straight toward origin (0,0)
        direction = Vector2D(0,0).sub(self.pos).normalized()
        distance_moved = self.speed * minute
        new_pos = self.pos.add(direction.scaled(distance_moved))
        return new_pos

    def distance_at(self, minute: float) -> float:
        return self.position_at(minute).norm()

    def is_in_vulnerable_range_at(self, minute: float, R: float) -> bool:
        # Checks if center is within the less than or equal range R
        return self.distance_at(minute) <= R

class LaserDefense:
    def __init__(self, R: float, ufos: List[UFO]):
        self.R = R
        self.ufos = ufos
        self.time = 0

    def all_ufos_alive(self) -> List[UFO]:
        return [u for u in self.ufos if u.alive]

    def find_next_target(self, current_time: float) -> Optional[UFO]:
        candidates = [u for u in self.all_ufos_alive() if not u.is_in_vulnerable_range_at(current_time, self.R)]
        if not candidates:
            return None
        # Select UFO with minimal distance at current time
        target = min(candidates, key=lambda u: u.distance_at(current_time))
        # Guarantee no ties as stated by problem
        return target

    def simulate(self) -> int:
        # Start firing at t=1 and then every 1 minute
        time = 1.0
        max_step = 10000  # safeguard to avoid infinite loops if weird data
        steps = 0
        while steps < max_step:
            steps += 1

            # Destroy all UFOs on the line of laser if any target found
            target = self.find_next_target(time)
            if target is None:
                # no more UFOs alive outside the R radius, finished
                break
            # Laser line: from origin to target center at current time
            target_pos = target.position_at(time)

            # Compute laser direction unit vector
            direction = target_pos.normalized()

            # Shoot laser and destroy all UFOs intersected by laser line
            for ufo in self.all_ufos_alive():
                ufo_pos = ufo.position_at(time)
                # Distance from origin along laser direction
                proj_len = ufo_pos.x * direction.x + ufo_pos.y * direction.y
                if proj_len < 0:
                    continue  # UFO behind the laser cannon, ignore
                # Closest distance from UFO center to laser line is the distance from center to line
                # We compute perpendicular distance via vector projection
                perp_vec = ufo_pos.sub(direction.scaled(proj_len))
                perp_dist = perp_vec.norm()
                if perp_dist <= ufo.radius:
                    # UFO hit and destroyed
                    ufo.alive = False
            time += 1

        # Count number of UFOs ever entering the no-power radius R (while alive or dead?)
        # Problem states those that were not destroyed and ended up <= R radius.
        # But simultaneity unclear: we take final alive UFOs within R at the end.
        count = 0
        for ufo in self.ufos:
            # Check position at the time laser started (1) and after simulation end
            # But problem suggests "after finishing all shooting", so check final time step -1 is fine
            # Because laser fires at times 1,2,... and then stops when no targets outside R left.
            # So use time-1 as final check time
            final_pos = ufo.position_at(time-1)
            if ufo.alive and final_pos.norm() <= self.R:
                count += 1
        return count

def parse_input() -> List[Tuple[float,int,List[UFO]]]:
    datasets = []
    input_lines = (line.rstrip('\n') for line in sys.stdin)
    while True:
        try:
            header = next(input_lines)
            if header == '':
                continue
            RN = header.split()
            if len(RN) != 2:
                continue
            R, N = int(RN[0]), int(RN[1])
            if R == 0 and N == 0:
                break
            ufos = []
            for _ in range(N):
                xi, yi, ri, vi = map(int, next(input_lines).split())
                ufos.append(UFO(Vector2D(xi, yi), ri, vi))
            datasets.append((R, N, ufos))
        except StopIteration:
            break
    return datasets

def main():
    datasets = parse_input()
    for R, N, ufos in datasets:
        defense = LaserDefense(R, ufos)
        result = defense.simulate()
        print(result)

if __name__ == '__main__':
    main()