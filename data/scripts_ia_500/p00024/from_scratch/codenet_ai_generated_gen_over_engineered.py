from abc import ABC, abstractmethod
from math import ceil
import sys

class PhysicsModel(ABC):
    @abstractmethod
    def velocity(self, t: float) -> float:
        pass

    @abstractmethod
    def drop(self, t: float) -> float:
        pass

class FreeFallPhysics(PhysicsModel):
    GRAVITY: float = 9.8

    def velocity(self, t: float) -> float:
        return self.GRAVITY * t

    def drop(self, t: float) -> float:
        return 0.5 * self.GRAVITY * t**2

class Building(ABC):
    @abstractmethod
    def height(self, floor: int) -> float:
        pass

class LinearHeightBuilding(Building):
    def __init__(self, base_height: float = 5.0, height_per_floor: float = 5.0):
        self.base_height = base_height
        self.height_per_floor = height_per_floor

    def height(self, floor: int) -> float:
        # Height of Nth floor is 5 * N - 5
        return self.height_per_floor * floor - self.base_height

class CrackDetector(ABC):
    @abstractmethod
    def floor_to_crack(self, min_velocity: float) -> int:
        pass

class FallingBallCrackDetector(CrackDetector):
    def __init__(self, physics: PhysicsModel, building: Building):
        self.physics = physics
        self.building = building

    def floor_to_crack(self, min_velocity: float) -> int:
        # minimal t to achieve min_velocity
        t = min_velocity / self.physics.GRAVITY
        drop_height = self.physics.drop(t)

        # Determine smallest floor whose height >= drop_height
        # Solve for floor in height formula: 5*floor -5 >= drop_height -> floor >= (drop_height + 5)/5
        floor = ceil((drop_height + 5) / 5)
        return floor

class InputProcessor:
    def __init__(self, detector: CrackDetector):
        self.detector = detector

    def process(self, lines):
        results = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            min_vel = float(line)
            floor = self.detector.floor_to_crack(min_vel)
            results.append(floor)
        return results

class OutputFormatter:
    def format(self, floors):
        for f in floors:
            print(f)

def main():
    physics = FreeFallPhysics()
    building = LinearHeightBuilding()
    detector = FallingBallCrackDetector(physics, building)
    processor = InputProcessor(detector)
    output = OutputFormatter()

    lines = sys.stdin.readlines()
    floors = processor.process(lines)
    output.format(floors)

if __name__ == "__main__":
    main()