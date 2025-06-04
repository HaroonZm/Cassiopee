from math import cos, sin, radians
from abc import ABC, abstractmethod
import sys

class Vector2D:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def scale(self, factor: float) -> 'Vector2D':
        return Vector2D(self.x * factor, self.y * factor)

    def rotate(self, degree: float) -> 'Vector2D':
        rad = radians(degree)
        cos_r = cos(rad)
        sin_r = sin(rad)
        return Vector2D(self.x * cos_r - self.y * sin_r, self.x * sin_r + self.y * cos_r)

    def __repr__(self):
        return f"Vector2D(x={self.x}, y={self.y})"

class DirectionProvider(ABC):
    @abstractmethod
    def get_direction(self, step_index: int) -> Vector2D:
        pass

class WellDirectionProvider(DirectionProvider):
    """
    Provides direction vector always towards the well placed at origin (0,0)
    from current position.
    """
    def __init__(self, well_position: Vector2D = Vector2D(0,0)):
        self.well_position = well_position

    def get_direction(self, step_index: int) -> Vector2D:
        # Return normalized vector from current position to well
        # Because we will always 'face' well, direction is from current position to well
        # In practice caller knows current position and reorients accordingly, so this
        # function by spec just returns the direction vector of the well which is always constant (origin)
        # So caller must calculate vector from current to well
        return Vector2D(0,0)  # Placeholder - actual usage elsewhere

class Navigator:
    def __init__(self, direction_provider: DirectionProvider):
        self.position = Vector2D(0.0, 0.0)
        self.direction_provider = direction_provider
        self.facing = Vector2D(1.0, 0.0)  # initially facing east

    def face_well(self):
        # Reorient facing vector to point directly from current position to well (0,0)
        vec_to_well = Vector2D(0.0, 0.0) - self.position
        length = (vec_to_well.x ** 2 + vec_to_well.y ** 2) ** 0.5
        if length == 0:
            # Already at well position
            self.facing = Vector2D(0,0)
        else:
            self.facing = Vector2D(vec_to_well.x / length, vec_to_well.y / length)

    def turn_right_90(self):
        # Rotate facing 90 degrees clockwise (right)
        self.facing = self.facing.rotate(-90)

    def move_forward(self, distance: float) -> bool:
        # Move forward distance in facing direction if possible.
        # The problem mentions possible obstruction but does not provide criteria, 
        # so assume always possible (no obstacle).
        delta = self.facing.scale(distance)
        self.position += delta
        return True

    def perform_step(self):
        # Turn right 90 degrees
        self.turn_right_90()
        # Move 1m forward
        self.move_forward(1.0)
        # Face well again
        self.face_well()

class TreasureHunter:
    def __init__(self, n: int):
        if not (2 <= n <= 1000):
            raise ValueError("n must be between 2 and 1000 inclusive")
        self.n = n
        self.navigator = Navigator(WellDirectionProvider())

    def find_treasure(self) -> Vector2D:
        # Initial step: from well, go east 1m, face well
        self.navigator.position = Vector2D(1.0, 0.0)
        self.navigator.face_well()
        # Then for n-1 times: turn right 90, move 1, face well
        for _ in range(self.n -1):
            self.navigator.perform_step()
        return self.navigator.position

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    count = 0
    for line in input_lines:
        if line.strip() == '-1':
            break
        n = int(line.strip())
        hunter = TreasureHunter(n)
        pos = hunter.find_treasure()
        print(f"{pos.x:.2f}")
        print(f"{pos.y:.2f}")
        count += 1
        if count >= 50:
            break

if __name__ == "__main__":
    main()