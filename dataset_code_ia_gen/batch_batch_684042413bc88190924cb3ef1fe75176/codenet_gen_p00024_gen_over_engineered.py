from abc import ABC, abstractmethod
from typing import Optional, List, Iterator
import sys
import math

class PhysicsModel(ABC):
    @abstractmethod
    def velocity_after(self, time: float) -> float:
        pass

    @abstractmethod
    def drop_after(self, time: float) -> float:
        pass

class FreeFallModel(PhysicsModel):
    GRAVITY: float = 9.8
    
    def velocity_after(self, time: float) -> float:
        return self.GRAVITY * time
    
    def drop_after(self, time: float) -> float:
        return 0.5 * self.GRAVITY * time**2

class FloorHeightModel(ABC):
    @abstractmethod
    def height_of_floor(self, floor: int) -> float:
        pass

class LinearFloorHeightModel(FloorHeightModel):
    def height_of_floor(self, floor: int) -> float:
        # height = 5 * N - 5 according to problem statement
        return 5 * floor - 5

class CrackVelocityDeterminer:
    def __init__(self, physics_model: PhysicsModel, height_model: FloorHeightModel) -> None:
        self.physics_model = physics_model
        self.height_model = height_model

    def minimal_floor_to_crack(self, crack_velocity: float) -> Optional[int]:
        """
        Determine minimal floor number where the ball cracks.

        Given minimum velocity to crack, find smallest floor N such that
        velocity on hitting that floor is at least crack_velocity.
        """
        if crack_velocity <= 0:
            return None  # Invalid input based on problem constraints

        # Use velocity = g * t
        # height = 5*N - 5 = 0.5 * g * t^2
        # solve t from height: t = sqrt(2*height/g)
        # velocity at hitting floor: v = g * t = g * sqrt(2*height/g) = sqrt(2*g*height)
        # Need smallest N s.t sqrt(2*g*height) >= crack_velocity
        # i.e. height >= (crack_velocity^2) / (2*g)
        threshold_height = (crack_velocity**2) / (2 * self.physics_model.GRAVITY)

        # Now find minimal floor N s.t 5*N - 5 >= threshold_height => N >= (threshold_height + 5)/5
        floor = math.ceil((threshold_height + 5) / 5)

        # Floor number must be positive integer; if result < 1, return 1
        return max(floor, 1)

class InputProcessor:
    def __init__(self, crack_handler: CrackVelocityDeterminer) -> None:
        self.crack_handler = crack_handler

    def process_stream(self, input_stream: Iterator[str]) -> List[int]:
        results = []
        for line in input_stream:
            line = line.strip()
            if not line:
                continue
            try:
                crack_velocity = float(line)
                # Constraints: 0 < v < 200 (handled implicitly, but we skip invalid input)
                if crack_velocity <= 0 or crack_velocity >= 200:
                    continue
            except ValueError:
                continue
            floor = self.crack_handler.minimal_floor_to_crack(crack_velocity)
            if floor is not None:
                results.append(floor)
        return results

def main():
    physics_model = FreeFallModel()
    floor_model = LinearFloorHeightModel()
    crack_handler = CrackVelocityDeterminer(physics_model, floor_model)
    input_processor = InputProcessor(crack_handler)
    results = input_processor.process_stream(sys.stdin)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()