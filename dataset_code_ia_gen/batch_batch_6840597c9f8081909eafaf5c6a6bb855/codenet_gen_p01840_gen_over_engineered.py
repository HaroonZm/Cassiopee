class TimeInterval:
    def __init__(self, start: int, end: int):
        if end < start:
            raise ValueError("End time must be greater than or equal to start time")
        self.start = start
        self.end = end

    @property
    def length(self) -> int:
        return self.end - self.start

    def __repr__(self):
        return f"TimeInterval({self.start}, {self.end})"


class Mansion:
    def __init__(self, study_room_start: int, front_door_arrival_time: int, study_room_end: int):
        if not (0 <= study_room_start <= front_door_arrival_time <= study_room_end):
            raise ValueError("Invalid time order for the mansion timeline")
        self.study_room_start = study_room_start
        self.front_door_arrival_time = front_door_arrival_time
        self.study_room_end = study_room_end


class DeliverySchedule:
    def __init__(self, deliveries: list):
        self.deliveries = deliveries
        self.validate_deliveries()

    def validate_deliveries(self):
        if any(self.deliveries[i] >= self.deliveries[i+1] for i in range(len(self.deliveries) -1)):
            raise ValueError("Delivery times must be strictly increasing")


class TaroStudyPlanner:
    def __init__(self, num_deliveries: int, travel_time: int, total_time: int, delivery_times: list):
        self.num_deliveries = num_deliveries
        self.travel_time = travel_time
        self.total_time = total_time
        self.delivery_times = delivery_times

        self.mansion = Mansion(
            study_room_start=0,
            front_door_arrival_time=travel_time,
            study_room_end=total_time
        )
        self.delivery_schedule = DeliverySchedule(delivery_times)

    def _compute_study_intervals(self):
        # Taro is initially at study room at t=0, and must be at front door at each delivery time a_i
        intervals = []
        prev_end = 0
        for arrival in self.delivery_times:
            # Before moving to front door, Taro must leave study room at arrival - M
            leave_time = arrival - self.travel_time
            # Time spent studying before heading out
            if leave_time > prev_end:
                intervals.append(TimeInterval(prev_end, leave_time))
            # Wait at front door for delivery, then return study room at arrival + M
            prev_end = arrival + self.travel_time
        # After last delivery, Taro can study until T
        if prev_end < self.total_time:
            intervals.append(TimeInterval(prev_end, self.total_time))
        return intervals

    def max_study_time(self) -> int:
        intervals = self._compute_study_intervals()
        total_study = sum(interval.length for interval in intervals)
        return total_study


def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    N, M, T = map(int, input_lines[0].split())
    delivery_times = list(map(int, input_lines[1].split()))

    planner = TaroStudyPlanner(N, M, T, delivery_times)
    print(planner.max_study_time())

if __name__ == "__main__":
    main()