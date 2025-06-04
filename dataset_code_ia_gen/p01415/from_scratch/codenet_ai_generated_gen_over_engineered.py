from abc import ABC, abstractmethod
from typing import List, Tuple


class RunningSpeedModel(ABC):
    @abstractmethod
    def get_speed(self, time_since_last_carrot: float) -> float:
        pass


class RabbitSpeedModel(RunningSpeedModel):
    def __init__(self, base_speed: float, boosted_speed: float, boost_duration: float):
        self.U = base_speed
        self.V = boosted_speed
        self.T = boost_duration

    def get_speed(self, time_since_last_carrot: float) -> float:
        if time_since_last_carrot <= self.T:
            return self.V
        else:
            return self.U


class CarrotStorage:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.carrots = 0

    def can_store(self) -> bool:
        return self.carrots < self.capacity

    def store(self):
        if self.can_store():
            self.carrots += 1
        else:
            raise RuntimeError("Storage full")

    def use(self):
        if self.carrots > 0:
            self.carrots -= 1
        else:
            raise RuntimeError("No carrots stored")


class CourseSegment:
    def __init__(self, start: float, end: float):
        # start and end positions in meters
        self.start = start
        self.end = end
        self.length = end - start


class RunningCourse:
    def __init__(self, length: float, carrot_positions: List[float]):
        self.length = length
        self.carrot_positions = carrot_positions
        self.segments = self._create_segments()

    def _create_segments(self) -> List[CourseSegment]:
        segments = []
        prev = 0.0
        for pos in self.carrot_positions:
            segments.append(CourseSegment(prev, pos))
            prev = pos
        segments.append(CourseSegment(prev, self.length))
        return segments


class RabbitRunner:
    def __init__(self, speed_model: RabbitSpeedModel, storage_capacity: int, course: RunningCourse):
        self.speed_model = speed_model
        self.storage = CarrotStorage(storage_capacity)
        self.course = course
        self.N = len(course.carrot_positions)
        self.memo = dict()  # For dynamic programming memoization

    def _dp(self, idx: int, carrots_carried: int, last_carrot_time: float, current_time: float) -> float:
        """
        :param idx: index of next carrot to consider (0-based)
        :param carrots_carried: number of carrots currently carried (0 to K)
        :param last_carrot_time: time when last carrot was eaten (or -inf initially)
        :param current_time: accumulated time spent so far
        :return: minimal time to reach goal from current state
        """
        key = (idx, carrots_carried, last_carrot_time)
        if key in self.memo:
            return self.memo[key]

        # If all carrots considered, just run to goal from current position
        if idx == len(self.course.segments):
            # from segment idx-1 end to goal (actually last segment end to goal is zero length)
            segment = self.course.segments[-1]
            dist = segment.length
            time_since_last_eat = current_time - last_carrot_time if last_carrot_time >= 0 else float('inf')
            speed = self.speed_model.get_speed(time_since_last_eat)
            res = dist / speed
            self.memo[key] = res
            return res

        # Current segment: from prev carrot pos to carrot idx pos
        segment = self.course.segments[idx]
        dist = segment.length

        # elapsed time since last carrot eaten when starting this segment:
        time_since_last_eat = current_time - last_carrot_time if last_carrot_time >= 0 else float('inf')

        # We have two possible actions at carrot idx:
        # 1) Eat this carrot immediately (need to have carrot in storage, or pick newly without storing)
        #    Eating resets boost timer to zero.
        # 2) Not eat, possibly store it (if capacity allows) for future eating.
        #    Or not store (just skip).
        #
        # We try all these possibilities and pick minimum time.

        # First, compute time to run this segment for a given strategy of eating timing.
        # But note: eating takes no time. Boost timer counts from eating moment.

        min_time = float('inf')

        # Action A: Eat carrot at this position immediately
        # Check storage: can we eat it without storing? Either eat immediately and reset boost timer.
        # Actually carrot is at the end of this segment.

        # To compute time to run this segment: the speed changes depend on elapsed time since last carrot eaten.
        # But eating happens at the end of segment => speed applied during the segment is based on last carrot eaten.

        # We have to carefully compute travel time if speed changes during the segment when boost expires.

        def compute_segment_time(distance: float, time_since_last_eat_start: float) -> float:
            # speed = V while (time_since_last_eat <= T), else U
            # We run the segment at initially time_since_last_eat_start seconds elapsed since last eat
            # Boost expires at (T - time_since_last_eat_start) seconds into the segment if positive.
            if time_since_last_eat_start > self.speed_model.T:
                # no boost for this segment
                return distance / self.speed_model.U

            boost_remain = self.speed_model.T - time_since_last_eat_start
            dist_in_boost = self.speed_model.V * boost_remain
            if dist_in_boost >= distance:
                # full segment can be covered during boost speed
                return distance / self.speed_model.V
            else:
                # part boost speed, part normal speed
                remainder = distance - dist_in_boost
                return boost_remain + remainder / self.speed_model.U

        # 1) Eat carrot immediately at end of this segment
        # Check if we have carrot in storage or we pick it and immediately eat. Since picking is instantaneous and no penalty,
        # Actually, picking is automatic in problem description, so always can pick carrot when reaching location.
        # We can model two options of picking:
        #   - pick to store for later (if storage available)
        #   - pick and eat immediately (not storing)
        #
        # Eating immediately after segment means: time to run segment with current boost, then eat resets boost timer to 0

        # compute time to run segment with current boost info
        time_for_segment = compute_segment_time(dist, time_since_last_eat)

        # after segment time, we eat: last_carrot_time = current_time + time_for_segment
        # after eating, carrots_carried remains the same if we eat immediately without storing new carrot (just no change)
        # or decreases by one if we eat from stored carrots.

        # Eat without stored carrots means pick-and-eat immediately.

        # So two subcases here:
        # - Eat carrot immediately by picking and eating (carrots_carried unchanged)
        # - Eat carrot immediately by eating stored carrot (if carrots_carried>0)

        # Subcase 1: pick + eat immediately (carrots_carried unchanged)
        next_time = current_time + time_for_segment
        res1 = self._dp(idx+1, carrots_carried, next_time, next_time)

        min_time = min(min_time, time_for_segment + res1)

        # Subcase 2: eat stored carrot after segment if carrots_carried>0
        if carrots_carried > 0:
            # We run segment with boost timer same as above
            # After segment, we eat stored carrot: carrots_carried-1, last carrot time updated
            next_time = current_time + time_for_segment
            res2 = self._dp(idx+1, carrots_carried - 1, next_time, next_time)
            min_time = min(min_time, time_for_segment + res2)

        # 2) Not eat carrot at this segment
        # We run segment with current boost timer, and then pick carrot. We can opt to store it instantly if storage available,
        # or ignore it (do not pick, not store, no speed effect).
        #
        # a) Pick and store carrot if storage space available
        # b) Skip picking carrot at all

        # In both cases, speed during segment is with current boost parameters.

        time_for_segment_noeat = compute_segment_time(dist, time_since_last_eat)
        next_time_noeat = current_time + time_for_segment_noeat

        # a) pick and store carrot
        if carrots_carried < self.storage.capacity:
            res_store = self._dp(idx+1, carrots_carried + 1, last_carrot_time, next_time_noeat)
            min_time = min(min_time, time_for_segment_noeat + res_store)
        # b) skip picking
        res_skip = self._dp(idx+1, carrots_carried, last_carrot_time, next_time_noeat)
        min_time = min(min_time, time_for_segment_noeat + res_skip)

        self.memo[key] = min_time
        return min_time

    def find_min_time(self) -> float:
        # initial state:
        # idx=0 (first carrot segment),
        # carrots_carried=0
        # last_carrot_time = -inf (no carrot eaten yet)
        # current_time=0.0

        # Represent no carrot eaten by a large negative value to avoid float('inf') issues
        return self._dp(0, 0, -1e15, 0.0)


def parse_input() -> Tuple[int, int, int, int, int, int, List[int]]:
    import sys
    input = sys.stdin.readline
    N, K, T, U, V, L = map(int, input().split())
    carrots = [int(input()) for _ in range(N)]
    return N, K, T, U, V, L, carrots


def main():
    N, K, T, U, V, L, carrots = parse_input()
    course = RunningCourse(L, carrots)
    speed_model = RabbitSpeedModel(U, V, T)
    runner = RabbitRunner(speed_model, K, course)
    ans = runner.find_min_time()
    print(f"{ans:.9f}")


if __name__ == "__main__":
    main()