from abc import ABC, abstractmethod
from typing import List, Set, Tuple, Dict, Optional
from collections import deque


class ColorTransformation(ABC):
    @staticmethod
    @abstractmethod
    def transform(pair: Tuple[str, str]) -> str:
        pass


class BeetleColorRule(ColorTransformation):
    COLORS = {'r', 'g', 'b'}

    @staticmethod
    def transform(pair: Tuple[str, str]) -> str:
        if pair[0] == pair[1]:
            raise ValueError("Pair colors must be different for transformation")
        return (BeetleColorRule.COLORS - set(pair)).pop()


class Segment(ABC):
    @abstractmethod
    def get_color(self) -> str:
        pass

    @abstractmethod
    def set_color(self, color: str) -> None:
        pass


class BodySegment(Segment):
    def __init__(self, color: str):
        if color not in BeetleColorRule.COLORS:
            raise ValueError(f"Invalid color {color}")
        self._color = color

    def get_color(self) -> str:
        return self._color

    def set_color(self, color: str) -> None:
        if color not in BeetleColorRule.COLORS:
            raise ValueError(f"Invalid color {color}")
        self._color = color

    def __repr__(self):
        return self._color


class Caterpillar(ABC):
    @abstractmethod
    def get_segments(self) -> List[Segment]:
        pass

    @abstractmethod
    def clone(self) -> 'Caterpillar':
        pass

    @abstractmethod
    def get_state_str(self) -> str:
        pass


class ConcreteCaterpillar(Caterpillar):
    def __init__(self, colors: List[str]):
        self._segments = [BodySegment(c) for c in colors]

    def get_segments(self) -> List[Segment]:
        return self._segments

    def clone(self) -> 'ConcreteCaterpillar':
        return ConcreteCaterpillar([seg.get_color() for seg in self._segments])

    def get_state_str(self) -> str:
        return ''.join(seg.get_color() for seg in self._segments)

    def __repr__(self):
        return self.get_state_str()


class TransformationEngine(ABC):
    @abstractmethod
    def get_next_states(self, state: Caterpillar) -> List[Caterpillar]:
        pass


class BeetleTransformationEngine(TransformationEngine):
    def get_next_states(self, state: Caterpillar) -> List[Caterpillar]:
        segments = state.get_segments()
        next_states: List[Caterpillar] = []
        length = len(segments)

        # Identify all pairs of adjacent segments with different colors
        candidate_pairs_indices = []
        for i in range(length - 1):
            c1, c2 = segments[i].get_color(), segments[i + 1].get_color()
            if c1 != c2:
                candidate_pairs_indices.append(i)

        # For each candidate pair, generate a new state with those two segments changed
        for idx in candidate_pairs_indices:
            base_state = state.clone()
            pair = (base_state.get_segments()[idx].get_color(), base_state.get_segments()[idx + 1].get_color())
            new_color = BeetleColorRule.transform(pair)
            base_state.get_segments()[idx].set_color(new_color)
            base_state.get_segments()[idx + 1].set_color(new_color)
            next_states.append(base_state)

        return next_states


class StopConditionChecker(ABC):
    @abstractmethod
    def is_stop(self, state: Caterpillar) -> bool:
        pass


class SameColorStopConditionChecker(StopConditionChecker):
    def is_stop(self, state: Caterpillar) -> bool:
        first_color = state.get_segments()[0].get_color()
        return all(seg.get_color() == first_color for seg in state.get_segments())


class SimulationController:
    def __init__(self, engine: TransformationEngine,
                 stop_checker: StopConditionChecker):
        self.engine = engine
        self.stop_checker = stop_checker

    def minimum_time_to_stable(self, initial_state: Caterpillar) -> Optional[int]:
        if self.stop_checker.is_stop(initial_state):
            return 0

        visited: Set[str] = set()
        queue: deque[Tuple[Caterpillar, int]] = deque()
        queue.append((initial_state, 0))
        visited.add(initial_state.get_state_str())

        while queue:
            current_state, time = queue.popleft()
            next_states = self.engine.get_next_states(current_state)
            for next_state in next_states:
                state_str = next_state.get_state_str()
                if state_str in visited:
                    continue
                if self.stop_checker.is_stop(next_state):
                    return time + 1
                visited.add(state_str)
                queue.append((next_state, time + 1))
        return None


class InputDatasetProcessor:
    def __init__(self, controller: SimulationController):
        self.controller = controller

    def process_lines(self, lines: List[str]) -> List[str]:
        results = []

        for line in lines:
            trimmed = line.strip()
            if trimmed == '0':
                break
            initial_state = ConcreteCaterpillar(list(trimmed))
            time = self.controller.minimum_time_to_stable(initial_state)
            results.append(str(time) if time is not None else 'NA')
        return results


def main():
    import sys
    lines = [line.rstrip('\n') for line in sys.stdin]
    engine = BeetleTransformationEngine()
    stop_checker = SameColorStopConditionChecker()
    controller = SimulationController(engine, stop_checker)
    processor = InputDatasetProcessor(controller)
    results = processor.process_lines(lines)
    for res in results:
        print(res)


if __name__ == '__main__':
    main()